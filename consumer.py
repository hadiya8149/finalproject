from confluent_kafka import Consumer
from pymongo import MongoClient

from json import loads, dumps
import ast
import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from naive_bayes_scratch_oge import naive_bayes_predict, loglikelihood, logprior
consumer = Consumer(
    {
        'bootstrap.servers':'localhost:9092', 
        'group.id':'mygroup', 
        'auto.offset.reset':'earliest'
    })

vader_model = SentimentIntensityAnalyzer()

clean_text = []
consumer.subscribe(['testevent'])

def get_database():
    CONNECTION_STRING = "mongodb+srv://blabla:xxeOtlemQRxYPAMY@cluster0.m20qm5i.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    return client['reddit_posts']

try:
    db  = get_database()
    posts_collection = db["posts"]

except:
    print("could not connect to mongodb")

def clean_text(text):
    text = text.lower() # lower case
    text = re.sub(r'[^\w\s]', '', text) #remove punctuation marks
    text = re.sub(" +", " ", text) # remove multiple spaces
    text = re.sub(r'http\S+', '', text, flags=re.MULTILINE) # remove links
    stop_words = set(stopwords.words('english')) # remove stopwords
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

while True:
    msg = consumer.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    data = msg.value().decode('utf-8')
    post = ast.literal_eval(data)
    text = post["text"]
    text = clean_text(text)
    bayes_score = naive_bayes_predict(text, logprior, loglikelihood)
    try:
        data = {
            "title":post["title"],
            "text": post["text"],
            "score":bayes_score
        }
        posts_collection.insert_one(data)
    except:
        print("could not insert into mongodb")

consumer.close()
