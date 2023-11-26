
import os
from dotenv import load_dotenv
from pymongo import MongoClient
import pandas as pd
load_dotenv()


def get_database():
    CONNECTION_STRING = os.getenv('MONGO_URI')

    client = MongoClient(CONNECTION_STRING)
    return client['reddit_posts']



try:
   
    db= get_database()
except:
    print("could not connect to mongodb")

cursor = db["posts_Jokes"].find()
df = pd.DataFrame(list(cursor))
breakpoint()
print(df.score.nunique())

# we want to group the data]
# i want to group the text that has similar values to an array let's say a dictionary that has score value and then the dictionar of arrays. to group the sentiment category into 
#likey scores
# to do this i have frequency count of each score now let's sort in ascending order
# nw we have the smallest score to the greates score
# and it's frequency is also adjacent 
# so to create groups we read the frequency count then read those lines and append their text into an array so our dataframe becomes smaller,
# and then for showing we draw a number line