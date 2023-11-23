from confluent_kafka import Consumer
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import ast
import re
# import nltk
# nltk.download("stopwords")
from nltk.corpus import stopwords
import pickle
from model import naive_bayes_predict

lp = pickle.load(open('./logprior_imdb.pkl', 'rb'))
llk = pickle.load(open('./loglikelihood_imdb.pkl', 'rb'))
load_dotenv()
consumer = Consumer(
    {
        'bootstrap.servers':'localhost:9092', 
        'group.id':'newGroup', 
        'auto.offset.reset':'earliest',
    })


consumer.subscribe(['quickstart-events'])

def get_database(): 
    CONNECTION_STRING = os.getenv('MONGO_URI')

    client = MongoClient(CONNECTION_STRING)
    
    return client['reddit_posts']

try:
    db  = get_database()
    posts_collection = db["posts_Jokes"]
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
    
    data =[]
    records = consumer.consume(num_messages=100)
    print(type(records))
    for msg in records:
        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue
    
        msg = msg.value().decode('utf-8')
        post = ast.literal_eval(msg)
        text = post["text"]
        text = clean_text(text)
        
        bayes_score = naive_bayes_predict(text, lp,llk)
        data.append({
                "title":post["title"],
                "text": post["text"],
                "score":bayes_score,
                "created_at": post["created_utc"]
            })
    try:
        
        posts_collection.insert_many(data)

        print("inserting documents")
        
    except:
        print("could not insert documents  into mongodb")

consumer.close()