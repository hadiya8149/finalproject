from confluent_kafka import Producer
import praw
from time import sleep
import json
data = {}
reddit = praw.Reddit(
                 client_id="RYwplqMp-ThgglPOj6-ZTQ",
                client_secret="rKC3QsYyR9E9XsMY7nAO8v5A_cvYfg",
                password="TVsA/ZRHE2gEM7A", 
                user_agent="rsa dashboard by u/LiteratureChemical50",
                username="LiteratureChemical50",)
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
for submission in reddit.subreddit("bitcoin").hot(limit=1000):
        if submission.selftext == "":
            continue
        posts.append({
            "title": submission.title,
            "text": submission.selftext,
            "url": submission.url
        })

for post in posts:
    producer.poll(0)
    producer.produce('testevent', str(post).encode('utf-8'), callback=delivery_report)
  
producer.flush()