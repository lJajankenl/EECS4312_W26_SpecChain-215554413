"""checks required files/folders exist"""
import os

required_folders = [
    "data",
    "personas",
    "spec",
    "tests",
    "metrics",
    "src",
    "reflection"
]

required_files = [
    "data/reviews_raw.jsonl",
    "data/reviews_clean.jsonl",
    "data/dataset_metadata.json",
    "data/review_groups_manual.json",
    "data/review_groups_auto.json",
    "data/review_groups_hybrid.json",
    "personas/personas_manual.json",
    "personas/personas_auto.json",
    "personas/personas_hybrid.json",
    "spec/spec_manual.md",
    "spec/spec_auto.md",
    "spec/spec_hybrid.md",
    "tests/tests_manual.json",
    "tests/tests_auto.json",
    "tests/tests_hybrid.json",
    "metrics/metrics_manual.json",
    "metrics/metrics_auto.json",
    "metrics/metrics_hybrid.json",
    "metrics/metrics_summary.json",
    "src/00_validate_repo.py",
    "src/01_collect_or_import.py",
    "src/02_clean.py",
    "src/03_manual_coding_template.py",
    "src/04_personas_manual.py",
    "src/05_personas_auto.py",
    "src/06_spec_generate.py",
    "src/07_tests_generate.py",
    "src/08_metrics.py",
    "src/run_all.py",
    "reflection/reflection.md",
    "README.md"
]

print("Checking repository structure...")

all_found = True

for folder in required_folders:
    if os.path.isdir(folder):
        print(f"{folder}/ found")
    else:
        print(f"{folder}/ MISSING")
        all_found = False

for filepath in required_files:
    if os.path.exists(filepath):
        print(f"{filepath} found")
    else:
        print(f"{filepath} MISSING")
        all_found = False

if all_found:
    print("Repository validation complete")
else:
    print("Repository validation failed: some folders or files are missing")