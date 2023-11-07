from flask import Flask, render_template, request
from pymongo import MongoClient
import numpy as np
from utils import count_freqs
from producer import stream_posts
from wordcloud import WordCloud
import os
import multiprocessing
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
#here we already have the db instance and we know our data has been stored correctly so what we need to 

# posts_collection = db[f"posts"]
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

    # build word cloud of positive posts and negative posts separately
    posts = p_posts+n_posts
    p_labels = np.append(np.ones(len(p_posts)), np.zeros(len(n_posts)))

    pl = np.ones(len(posts))
    nl = np.zeros(len(n_posts))
    p_freqs = count_freqs({}, p_posts, pl)
    n_freqs = count_freqs({},n_posts, nl)
    freqs = count_freqs({}, posts, p_labels )
    pDict = {}
    nDict = {}
    p_vocab = set(pair[0] for pair in p_freqs.keys())
    n_vocab = set(pair[0] for pair in n_freqs.keys())
    for x,y in p_freqs.items():
        pDict[x[0]] =y
    for x,y in n_freqs.items():
        nDict[x[0]] =y
    tmpDict = {}
    vocab = set(pair[0] for pair in freqs.keys())
    for x,y in freqs.items():
        tmpDict[x[0]] = y
    V = len(p_vocab)

    pwc = WordCloud(max_words=len(pDict))
    text = " ".join(p_vocab)
    if pDict:
        pwc.generate_from_frequencies(pDict)
        pwc.to_file("./static/p_wc.png")
        nwc = WordCloud(max_words=len(nDict))
        text = " ".join(n_vocab)
        nwc.generate_from_frequencies(nDict)
        nwc.to_file("./static/n_wc.png")
    print("done processing")
    return data
data = []
def log_result(res):
    data.append(res)
@app.route("/", methods=['GET', 'POST'])

def home_page():
    if request.method == 'POST':
        query = request.form["query"]
        stream_posts(query)
        
        # data = process_data(db[f"posts_{query}_imdb"])
        
        pool = multiprocessing.Pool()
        pool.apply_async(process_data, args=(db[f"posts_{query}_imdb"]), callback=log_result)
        # pool.close()
        # pool.join()
        # print(data)
        

        return render_template("index.html", data=data) 
    else:
        return render_template("index.html", data={})
if __name__ == "__main__":
    app.debug=True
    app.run()