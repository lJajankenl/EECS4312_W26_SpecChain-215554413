import json
import os

AMBIGUOUS_WORDS = ["simple", "intuitive", "easy", "fast", "affordable", "personalized", "user-friendly", "clearly", "quickly"]

def count_reviews(jsonl_path):
    with open(jsonl_path) as f:
        return sum(1 for _ in f)

def parse_requirements(spec_path):
    with open(spec_path) as f:
        spec = f.read()
    return spec.split("# Requirement ID:")[1:]

def compute_ambiguity(requirements_blocks):
    ambiguous = 0
    for req in requirements_blocks:
        if any(word in req.lower() for word in AMBIGUOUS_WORDS):
            ambiguous += 1
    return ambiguous / len(requirements_blocks) if requirements_blocks else 0

def compute_review_coverage(personas, total_reviews):
    used_reviews = set()
    for persona in personas:
        used_reviews.update(persona.get("evidence_reviews", []))
    return len(used_reviews) / total_reviews if total_reviews > 0 else 0

def compute_traceability_links(requirements_blocks, persona_count):
    return (len(requirements_blocks) * 2) + persona_count

def compute_traceability_ratio(requirements_blocks):
    traced = sum(1 for req in requirements_blocks if "source persona" in req.lower() or "traceability" in req.lower())
    return traced / len(requirements_blocks) if requirements_blocks else 0

def compute_metrics(pipeline, spec_path, tests_path, personas_path, reviews_path, output_path):
    total_reviews = count_reviews(reviews_path)
    requirements_blocks = parse_requirements(spec_path)

    with open(tests_path) as f:
        raw_tests = json.load(f)
    tests = raw_tests if isinstance(raw_tests, list) else raw_tests.get("tests", [])

    with open(personas_path) as f:
        raw_personas = json.load(f)
    personas = raw_personas if isinstance(raw_personas, list) else raw_personas.get("personas", [])

    metrics = {
        "pipeline": pipeline,
        "dataset_size": total_reviews,
        "persona_count": len(personas),
        "requirements_count": len(requirements_blocks),
        "tests_count": len(tests),
        "traceability_links": compute_traceability_links(requirements_blocks, len(personas)),
        "review_coverage": round(compute_review_coverage(personas, total_reviews), 4),
        "traceability_ratio": round(compute_traceability_ratio(requirements_blocks), 4),
        "testability_rate": round(len(tests) / len(requirements_blocks), 4) if requirements_blocks else 0,
        "ambiguity_ratio": round(compute_ambiguity(requirements_blocks), 4)
    }

    if not os.path.exists(output_path):
        with open(output_path, "w") as f:
            json.dump(metrics, f, indent=4)

    return metrics


total_reviews_path = "data/reviews_clean.jsonl"

compute_metrics(
    pipeline="manual",
    spec_path="spec/spec_manual.md",
    tests_path="tests/tests_manual.json",
    personas_path="personas/personas_manual.json",
    reviews_path=total_reviews_path,
    output_path="metrics/metrics_manual.json"
)

compute_metrics(
    pipeline="automated",
    spec_path="spec/spec_auto.md",
    tests_path="tests/tests_auto.json",
    personas_path="personas/personas_auto.json",
    reviews_path=total_reviews_path,
    output_path="metrics/metrics_auto.json"
)

compute_metrics(
    pipeline="hybrid",
    spec_path="spec/spec_hybrid.md",
    tests_path="tests/tests_hybrid.json",
    personas_path="personas/personas_hybrid.json",
    reviews_path=total_reviews_path,
    output_path="metrics/metrics_hybrid.json"
)

def strip_pipeline_key(metrics):
    return {k: v for k, v in metrics.items() if k != "pipeline"}

with open("metrics/metrics_manual.json") as f:
    manual_metrics = json.load(f)

with open("metrics/metrics_auto.json") as f:
    auto_metrics = json.load(f)

with open("metrics/metrics_hybrid.json") as f:
    hybrid_metrics = json.load(f)

summary = {
    "manual": strip_pipeline_key(manual_metrics),
    "automated": strip_pipeline_key(auto_metrics),
    "hybrid": strip_pipeline_key(hybrid_metrics)
}

with open("metrics/metrics_summary.json", "w") as f:
    json.dump(summary, f, indent=4)