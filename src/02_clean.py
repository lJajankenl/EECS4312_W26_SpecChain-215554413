"""cleans raw data & make clean dataset"""
import pandas as pd
import num2words
from stop_words import get_stop_words
import nltk
import re
nltk.download('punkt_tab')      
nltk.download('wordnet')    
nltk.download('omw-1.4') 
nltk.download('averaged_perceptron_tagger_eng')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

df = pd.read_json("data/reviews_raw.jsonl", lines=True)
df.drop_duplicates(inplace=True)

df = df[df['content'].notna() & (df['content'] != '')]

# The valid review length must be greater than 20 because arbitrarily set.  
df = df[df['content'].str.len() > 20]

# Remove punctuation, special characters, and emojis.  
df['content'] = df['content'].str.replace(r"[^\w\s]", "", regex=True)

# Convert numbers to text
pattern = r"\d+"

def convert_numbers(review):
    numberMatches = re.findall(pattern, review)
    for number in numberMatches:
        word = num2words.num2words(int(number))
        review = review.replace(number, word)
    return review

df['content'] = df['content'].apply(convert_numbers)

# Remove extra whitespace

# Convert all words to lowercase
df['content'] = df['content'].str.lower()

# Remove stop words
#stop_words = get_stop_words('en')
#df['content'] = df['content'].str.replace(r"[stop_words]", "", regex=True)

# Lemmatize the reviews
lemmatizer = WordNetLemmatizer()
df['content'] = [lemmatizer.lemmatize(word) for word in df['content']]

df.to_json("data/reviews_clean.jsonl", orient="records", lines=True)