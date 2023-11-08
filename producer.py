from confluent_kafka import Producer
from dotenv import load_dotenv
import praw
import os
from pymongo import MongoClient

"""
In this file we fetch the data from reddit api and send it to kafka cluster using producer
"""
load_dotenv()
producer = Producer(
    {'bootstrap.servers':'localhost:9092'} 
                         )
# def get_database(): 
#     CONNECTION_STRING = os.getenv('MONGO_URI')

#     client = MongoClient(CONNECTION_STRING)
#     return client['reddit_posts']




# try:
#     db  = get_database()
    
# except:
#     print("could not connect to mongodb")

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print("Message delivered to {} [{}]".format(msg.topic(), msg.partition))



reddit = praw.Reddit(
                client_id=os.getenv("CLIENT_ID"),
                client_secret=os.getenv("CLIENT_SECRET"),
                password=os.getenv("PASSWORD"), 
                user_agent=os.getenv("USER_AGENT"),
                username=os.getenv("USERNAME"),)
print(reddit.user.me())

posts=[]
def stream_posts(query):
    
    for submission in reddit.subreddit(query).hot(limit=None):
        if submission.selftext == "":
            continue
        posts.append({
            "title": submission.title,
            "text": submission.selftext,
            "url": submission.url,
            "created_utc":submission.created_utc,
            "votes":submission.score,

        })
    print(len(posts))
    for post in posts:
        producer.poll(0)
        producer.produce('quickstart-events', str(post).encode('utf-8'), callback=delivery_report)
    
    producer.flush(0)
    return True