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
    elif err:
        print(err)
    else:
        print("Message delivered to {} [{}]".format(msg.topic(), msg.partition))


posts=[]
i = 0
for submission in reddit.subreddit("bitcoin").stream.submissions():
    if submission.selftext == "":
        continue
    i+=1
    print(submission.title, submission.selftext)
    post = {
        "title":submission.title,
        "text": submission.selftext,
        "url": submission.url
    }
    posts.append({
        "title": submission.title,
        "text": submission.selftext,
        "url": submission.url
    })
    print("sending")
    
    producer.poll(0)
    producer.produce('redditStream', str(post).encode('utf-8'), callback=delivery_report)

# for post in posts:
producer.flush(0)