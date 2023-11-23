from flask import Flask, render_template, request
from pymongo import MongoClient
from producer import stream_posts
import os
from dotenv import load_dotenv
app = Flask(__name__)

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
    data = [p,n]
    print("done processing")
    return data



@app.route("/", methods=['GET', 'POST'])

def home_page():
    
    if request.method == 'POST':
        query = request.form["query"]
        
        # flag = stream_posts(query)

        # if flag:
        data = get_scores(db[f"posts_{query}"])
        cursor =  list(db[f"posts_{query}"].find({}, {"_id":0, "title":1, "text":1, "score":1, "created_at":1}, limit=100))

        return render_template("/index.html", data=data, cursor=cursor, query=query) 
    else:
        cursor = list(db[f"posts_Jokes"].find({}, {"_id":0, "title":1, "text":1, "score":1, "created_at":1}, limit=100))

        return render_template("/index.html", data=[], cursor=cursor, query="sample")
if __name__ == "__main__":
    app.debug=True
    app.run()
