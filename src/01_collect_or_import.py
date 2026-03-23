"""imports or reads your raw dataset; if you scraped, include scraper here"""
from google_play_scraper import app
import pandas as pd
import numpy as np 

from google_play_scraper import Sort, reviews_all


calm_reviews = reviews_all(
    'com.calm.android',
    sleep_milliseconds=0, # defaults to 0
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
) 
df_calm = pd.DataFrame(np.array(calm_reviews),columns=['review'])


df_calm = df_calm.join(pd.DataFrame(df_calm.pop('review').tolist()))
df_calm.to_json("data/reviews_raw.jsonl", orient="records", lines=True)

