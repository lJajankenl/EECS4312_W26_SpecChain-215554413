"""creates/updates coding table template + instructions"""
import pandas as pd

df = pd.read_json("data/reviews_clean.jsonl", lines=True)