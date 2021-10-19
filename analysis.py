import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

results = pd.read_csv(r'IMDB_scraper\movies.csv')

counts = results.groupby("movie_or_TV_name").apply(len).reset_index()
counts = counts.rename(columns={0:"count"}).sort_values(by="count", ascending=False)
counts

the_title = counts.iloc[0,0]

counts = counts[counts.apply(lambda x: the_title not in x["movie_or_TV_name"] and x["count"] > min([5, max(counts["count"])/4]), axis=1)]

for count, value in enumerate(counts["movie_or_TV_name"][:20]):
    print(count, value)