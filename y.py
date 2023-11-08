# we can build word clouds for the titles also

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
        nwc.generate_from_frequencies(nDict)
        nwc.to_file("./static/n_wc.png")
    print("done processing")
    return data