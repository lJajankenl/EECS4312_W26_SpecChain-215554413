# EECS4312_W26_SpecChain

Application: Calm - Sleep, Meditate, Relax

Dataset:
- reviews_raw.jsonl contains the collected reviews.
- reviews_clean.jsonl contains the cleaned dataset.
- The raw dataset contains 2000 reviews.
- The cleaned dataset contains 1520 reviews.

Repository Structure:
- data/ contains datasets, review groups, and metadata.  
- personas/ contains persona files for the manual, automated, and hybrid pipelines
- spec/ contains specifications for the manual, automated, and hybrid pipelines
- tests/ contains validation tests for the manual, automated, and hybrid pipelines
- metrics/ contains all metric files for the manual, automated, and hybrid pipelines
- src/ contains executable Python scripts
- reflection/ contains the final reflection


How to Run:

To validate the repository structure: 
python src/00_validate_repo.py

To run the full automated pipeline:
python src/run_all.py

To view the metrics comparison across all three pipelines:
metrics/metrics_summary.json