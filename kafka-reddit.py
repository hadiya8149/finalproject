from confluent_kafka import Producer
import praw
from dotenv import load_dotenv
import os
load_dotenv()
data = {}
reddit = praw.Reddit(
                client_id=os.getenv("CLIENT_ID"),
                client_secret=os.getenv("CLIENT_SECRET"),
                password=os.getenv("PASSWORD"), 
                user_agent=os.getenv("USER_AGENT"),
                username=os.getenv("USERNAME"),)
print(reddit.user.me())
producer = Producer(
    {'bootstrap.servers':'localhost:9092'} 
                         )
def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print("Message delivered to {} [{}]".format(msg.topic(), msg.partition))


posts=[]

"""
for submission in reddit.subreddit("bitcoin").stream.submissions():
     if submission.selftext == "":
        continue
    post = {
        "title": submission.title,
        "text": submission.selftext,
        "url": submission.url

    # i will also add the timestammp in later coding phase
    # this code is for realtime streaming to kafka but the problem is duplicated posts so i haven't implemented it yet
    producer.poll(0)
    producer.produce('redditStream', str(post).encode('utf-8'), callback=delivery_report)
    }

"""
for submission in reddit.subreddit("bitcoin").hot(limit=None):
    if submission.selftext == "":
        continue
    posts.append({
        "title": submission.title,
        "text": submission.selftext,
        "url": submission.url
    })

print(len(posts))
for post in posts:
    producer.poll(0)
    producer.produce('redditStream', str(post).encode('utf-8'), callback=delivery_report)

producer.flush(0)