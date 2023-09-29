# import pandas as pd
# import numpy as np

# misc
import datetime as dt
from pprint import pprint
from itertools import chain

# reddit crawler
import praw

# sentiment analysis
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize, RegexpTokenizer # tokenize words
from nltk.corpus import stopwords
reddit = praw.Reddit(
                 client_id="RYwplqMp-ThgglPOj6-ZTQ",
                client_secret="rKC3QsYyR9E9XsMY7nAO8v5A_cvYfg",
                password="TVsA/ZRHE2gEM7A",
                user_agent="rsa dashboard by u/LiteratureChemical50",
                username="LiteratureChemical50",)
print(reddit.user.me())
subreddit = reddit.subreddit('technews')

news = [*subreddit.top(limit=None)] # top posts all time

print(len(news))
news0 = news[0]
for  i in range(1, 10):
    print(news[i])
# pprint(vars(news0)) 
print(news0.title) # headline
print(news0.score) # upvotes
print(news0.created) # UNIX timestamps 
print(dt.datetime.fromtimestamp(news0.created)) # date and time
print(news0.num_comments) # no. of comments
print(news0.upvote_ratio) # upvote / total votes
print(news0.total_awards_received) # no. of awards given
# print(len(news)) 
# visualization
# import matplotlib.pyplot as plt
# plt.rcParams["figure.figsize"] = (10, 8) # default plot size
# import seaborn as sns
# sns.set(style='whitegrid', palette='Dark2')
# from wordcloud import WordCloud