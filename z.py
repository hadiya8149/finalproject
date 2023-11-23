
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from utils import process_text
load_dotenv()


def get_database():
    CONNECTION_STRING = os.getenv('MONGO_URI')

    client = MongoClient(CONNECTION_STRING)
    return client['reddit_posts']



try:
   
    db= get_database()
except:
    print("could not connect to mongodb")


def get_scores(collection): 
    cursor = list(collection.find())
    p = []
    n = []
    p_posts = []
    n_posts=[]
    for i in cursor:
        if i["score"] <=0:
            n.append(i["score"])
            n_posts.append(i["text"])
        else:
            p.append(i["score"])
            p_posts.append(i["text"])
    print(len(p), len(n))
    p.sort()
    n.sort()
    data = [p,n]
    print("done processing")
    return data

scores=get_scores(db[f"posts_Jokes"])

cursor = list(db[f"posts_Jokes"].find({}, {"text":1}, limit=100))
arr = []
for i in cursor:
    print(i["text"])
    arr.append(i["text"])
print("This is arr")
print(arr)



# we want to group the data]