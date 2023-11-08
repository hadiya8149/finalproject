from flask import Flask, render_template, request
from pymongo import MongoClient
import numpy as np
from utils import count_freqs
from producer import stream_posts
from wordcloud import WordCloud
import os
from dotenv import load_dotenv
app = Flask(__name__)
load_dotenv()

def get_database(): 
    CONNECTION_STRING = os.getenv('MONGO_URI')

    client = MongoClient(CONNECTION_STRING)
    return client['reddit_posts']




try:
    db  = get_database()
    
except:
    print("could not connect to mongodb")

def process_data(collection):
# store data of positve and negative sentimetns

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
    data = [p,n]
    print("done processing")
    return data
collection = db["posts_drugs_imdb"]

data = process_data(collection)
print(data)
@app.route("/", methods=['GET', 'POST'])

def home_page():
    
    if request.method == 'POST':
        query = request.form["query"]
        flag = stream_posts(query)
        
        return render_template("index.html", data=data) 
    
    return render_template("index.html", data=data)
if __name__ == "__main__":
    app.debug=True
    app.run()