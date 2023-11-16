from flask import Flask, render_template, request
from pymongo import MongoClient
import pandas as pd
from utils import count_freqs
from producer import stream_posts
from wordcloud import WordCloud
import os
from dotenv import load_dotenv
app = Flask(__name__)
load_dotenv()
# so we have one collection here and the data of that collection is first processed to get the stores and then all of the data is stored in table so why not just do it in first try!
def get_database(): 
    CONNECTION_STRING = os.getenv('MONGO_URI')

    client = MongoClient(CONNECTION_STRING)
    return client['reddit_posts']




try:
    db  = get_database()
    
except:
    print("could not connect to mongodb")


def get_scores(collection): # it builds chart

    cursor = list(collection.find())
    breakpoint()
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
# 

# data = process_data(collection)
def get_collection(query):
    coll = db[f"posts_{query}"]

    return coll
collection = get_collection("drugs_ts")
x = list(collection.find())
df = pd.DataFrame(x)
print(df.head())
tables=[df.to_html(columns=['title','text', 'score', 'created_at'])]

@app.route("/", methods=['GET', 'POST'])

def home_page():
    
    if request.method == 'POST':
        query = request.form["query"]
        
        flag = stream_posts(query)
        
        if flag:
            data = get_scores(db[f"posts_{query}"])
        
        return render_template("index.html", data=data) 
    else:
        
        return render_template("index.html", data=[], tables =tables)
if __name__ == "__main__":
    app.debug=True
    app.run()