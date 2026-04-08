"""runs the full pipeline end-to-end"""
# Step 1: Collect/import raw reviews -> data/reviews_raw.jsonl
exec(open("src/01_collect_or_import.py").read())

# Step 2: Clean raw reviews -> data/reviews_clean.jsonl
exec(open("src/02_clean.py").read())

# Step 3: Generate automated personas from review groups -> personas/personas_auto.json
exec(open("src/05_personas_auto.py").read())

# Step 4: Generate automated specifications from personas -> spec/spec_auto.md
exec(open("src/06_spec_generate.py").read())

# Step 5: Generate automated tests from specifications -> tests/tests_auto.json
exec(open("src/07_tests_generate.py").read())

# Step 6: Compute metrics for all pipelines and save summary -> metrics/
exec(open("src/08_metrics.py").read())

# Step 7: Validate that all required folders and files are present
exec(open("src/00_validate_repo.py").read())