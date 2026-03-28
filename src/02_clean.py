"""cleans raw data & make clean dataset"""
import pandas as pd
import num2words

df = pd.read_json("data/reviews_raw.jsonl", lines=True)
df.drop_duplicates(inplace=True)

df = df[df['content'].notna() & (df['content'] != '')]

# The valid review length must be greater than 20 because arbitrarily set.  
df = df[df['content'].str.len() > 20]

# Remove punctuation, special characters, and emojis.  
df['content'] = df['content'].str.replace(r"[^\w\s]", "", regex=True)

# Convert numbers to text
#df['content'] = df['content'].str.replace(r"\d+", num2words(), regex=True)

# Remove extra whitespace

# Convert all words to lowercase
df['content'] = df['content'].str.lower()

# Remove stop words

# Lemmatize the reviews

df.to_json("data/reviews_clean.jsonl", orient="records", lines=True)