"""generates tests from specs"""
import json
import re

with open("spec/spec_auto.md") as f:
    specs = f.read()

specs = specs.split("\n\n")

tests = []

for spec in specs:
    lines = spec.splitlines()
    if len(lines) < 5:
        continue

    requirement_id = lines[0].split(": ")[1]
    description = lines[1].split(": ")[1]
    source_persona = lines[2].split(": ")[1]
    traceability = lines[3].split(": ")[1]
    acceptance_criteria = lines[4].split(": ")[1].strip("[]").split(", ")

    given_clause = acceptance_criteria[0].strip()
    when_clause = acceptance_criteria[1].strip()
    then_clause = acceptance_criteria[2].strip()

    test_id = f"TEST-{requirement_id}"
    scenario_description = f"Verify that {description} for {source_persona}"

    steps = [
        f"1. {given_clause}",
        f"2. {when_clause}",
        f"3. Verify that {then_clause}"
    ]

    expected_outcome = then_clause

    test = {
        "test_id": test_id,
        "requirement_id": requirement_id,
        "scenario_description": scenario_description,
        "steps": steps,
        "expected_outcome": expected_outcome
    }

    tests.append(test)

with open("tests/tests_auto.json", "w") as f:
    json.dump(tests, f, indent=4)