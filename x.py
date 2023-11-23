from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()
import concurrent.futures

def get_database(): 
    CONNECTION_STRING = os.getenv('MONGO_URI')

    client = MongoClient(CONNECTION_STRING)
    return client['reddit_posts']




try:
    db  = get_database()
    coll = db["posts_drugs_ts"]
except:
    print("could not connect to mongodb")
# now we want threads here to fetch the data in as little time as possible


def get_data(n):
    x =coll.find({}, {"_id":0, "title":1, "text":1, "score":1, "created_at":1}, skip=n, limit=100)
    return x
cursors = []
# x = coll.find({}, {"_id":0, "title":1, "text":1, "score":1, "created_at":1})
# # for i in x:
# #     y.append(i["score"])
params = [0,100,200,300,400,500,600,700]
table = []
def dummy(c):
    table.append(list(c))
    return table
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executer:
    future_to_x = {executer.submit(get_data, n): n for n in params}
    for future in concurrent.futures.as_completed(future_to_x):
        res = future_to_x[future]
        try:
            data = future.result()
            cursors.append(data)
        except Exception as exc:
            print('%r generated an exception: %s' %(res, exc))
        else:
            print("cursor", data)

    
print(len(cursors))

# now we can iterate through cursors 
# print(len(y))