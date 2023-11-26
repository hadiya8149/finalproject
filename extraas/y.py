# we can build word clouds for the titles also
import numpy as np
import pandas as pd
from pymongo import MongoClient
import os
from dotenv import load_dotenv
from utils import *
load_dotenv()
def get_database():
    CONNECTION_STRING = os.getenv('MONGO_URI')

    client = MongoClient(CONNECTION_STRING)
    return client['reddit_posts']



try:
   
    db= get_database()
except:
    print("could not connect to mongodb")

def process_data():
# store data of positve and negative sentimetns

    cursor = list(db[f"posts_Jokes"].find({}, {"text":1, "score":1}, limit=100))
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
    p.sort()
    n.sort()
    print(len(p),p[0], "-", p[-1],n[0],"-", n[-1] ,len(n))
    data = [p,n]

    # # build word cloud of positive posts and negative posts separately
    # posts = p_posts+n_posts
    # p_labels = np.append(np.ones(len(p_posts)), np.zeros(len(n_posts)))

    # pl = np.ones(len(posts))
    # nl = np.zeros(len(n_posts))
    # p_freqs = count_freqs({}, p_posts, pl)
    # n_freqs = count_freqs({},n_posts, nl)
    # freqs = count_freqs({}, posts, p_labels )
    # pDict = {}
    # nDict = {}
    # p_vocab = set(pair[0] for pair in p_freqs.keys())
    # n_vocab = set(pair[0] for pair in n_freqs.keys())
    # for x,y in p_freqs.items():
    #     pDict[x[0]] =y
    # for x,y in n_freqs.items():
    #     nDict[x[0]] =y
    # tmpDict = {}
    # vocab = set(pair[0] for pair in freqs.keys())
    # for x,y in freqs.items():
    #     tmpDict[x[0]] = y
    # pv = len(p_vocab)
    # nv = len(n_vocab)
    # print(pv)
    # print(pDict)
    # print(pDict.keys())
    
    # pwc = WordCloud(max_words=len(pDict))
    # text = " ".join(p_vocab)
    # if pDict:
    #     pwc.generate_from_frequencies(pDict)
    #     pwc.to_file("./static/p_wc.png")
    #     nwc = WordCloud(max_words=len(nDict))
    #     nwc.generate_from_frequencies(nDict)
    #     nwc.to_file("./static/n_wc.png")
    # print("done processing")
    return data
x = process_data()