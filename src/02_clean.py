"""cleans raw data & make clean dataset"""
import pandas as pd
import num2words
from stop_words import get_stop_words
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')
import re

df = pd.read_json("data/reviews_raw.jsonl", lines=True)

# Remove duplicate reviews
df.drop_duplicates(inplace=True)

# Remove empty reviews
df = df[df['content'].notna() & (df['content'] != '')]

# Removes short reviews, i.e., reviews that have 20 or less characters.  
df = df[df['content'].str.len() > 20]

# Removes punctuation, special characters, and emojis 
df['content'] = df['content'].str.replace(r"[^\w\s]", "", regex=True)

# Convert numbers to text
numberPattern = r"\d+"

def convert_numbers(review):
    numberMatches = re.findall(numberPattern, review)
    for number in numberMatches:
        word = num2words.num2words(int(number))
        review = review.replace(number, word)
    return review

df['content'] = df['content'].apply(convert_numbers)

# Remove extra whitespace
df['content'] = df['content'].str.replace(r"\s+", " ", regex=True)
df['content'] = df['content'].str.strip()

# Convert all words to lowercase
df['content'] = df['content'].str.lower()

# Removes stop words
stop_words = set(stopwords.words('english'))
filtered_reviews = []

for review in df['content']:
    word_tokens = word_tokenize(review)
    
    filtered_words = []
    for word in word_tokens:
        if word not in stop_words:
            filtered_words.append(word)

    filtered_reviews.append(" ".join(filtered_words))
df['content'] = filtered_reviews


# Lemmatize the reviews
#lemmatizer = WordNetLemmatizer()
#df['content'] = [lemmatizer.lemmatize(word) for word in df['content']]

df.to_json("data/reviews_clean.jsonl", orient="records", lines=True)