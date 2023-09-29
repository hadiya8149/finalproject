import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
txt = "Describe Elon Musk (me) using one word…"
vader_model = SentimentIntensityAnalyzer()
score = vader_model.polarity_scores(txt)
print(score)
# add them to database
# read the data from database and visualize it
