from pymongo import MongoClient
import os
from dotenv import load_dotenv
import pandas as pd
load_dotenv()

def get_database(): 
    CONNECTION_STRING = os.getenv('MONGO_URI')

    client = MongoClient(CONNECTION_STRING)
    return client['reddit_posts']




try:
    db  = get_database()
    coll = db["posts_drugs_ts"]
except:
    print("could not connect to mongodb")
count =0
# now we want threads here to fetch the data in as little time as possible


def get_scores(cursor): # pass a cursor and get all the numerical scores 
    # we can also get the score by selecting a single column and then iterating it

    pass

x =list(coll.find({}, {"_id":0, "title":1, "text":1, "score":1, "created_at":1}, limit=100))
y=[]
df = pd.DataFrame(x)

# for i in x:
#     # we get the score and then we append the data to a dataframe at the same time
#     y.append(i["score"])
#     # df = df._append(i, ignore_index=True)
    

print(y)
print(len(y))
print(df.head())   



def make_table(): # pass a cursor and write all the data in a table we using dataframe here so it's a csv file
    pass


def build_word_cloud(): 
    pass