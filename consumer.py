from confluent_kafka import Consumer
from pymongo import MongoClient
from dotenv import load_dotenv
import os

import ast
import re
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from naive_bayes_scratch import naive_bayes_predict, loglikelihood, logprior
load_dotenv()
consumer = Consumer(
    {
        'bootstrap.servers':'localhost:9092', 
        'group.id':'redditgroup', 
        'auto.offset.reset':'earliest'
    })

vader_model = SentimentIntensityAnalyzer()

clean_text = []
consumer.subscribe(['redditStream'])

def get_database(): 
    CONNECTION_STRING = os.getenv('MONGO_URI')

    client = MongoClient(CONNECTION_STRING)
    
    return client['reddit_posts']

try:
    db  = get_database()
    posts_collection = db["posts_10/18/2023"]
    print("connected to database")
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
            "score":bayes_score,
            "created_at": post.created_utc
        }
        posts_collection.insert_one(data)
        print("inserting document")
    except:
        print("could not insert into mongodb")

consumer.close()
