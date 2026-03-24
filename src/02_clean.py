"""cleans raw data & make clean dataset"""
import pandas as pd

df = pd.read_json("data/reviews_raw.jsonl", lines=True)
df.drop_duplicates(inplace=True)

df = df[df['content'].notna() & (df['content'] != '')]

# The valid review length must be greater than 20 because arbitrarily set.  
df = df[df['content'].str.len() > 20]

df.to_json("data/reviews_clean.jsonl", orient="records", lines=True)