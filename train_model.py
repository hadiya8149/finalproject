import numpy as np
import pandas as pd
from utils import lookup, count_freqs
# from nltk.corpus import  twitter_samples
import pickle



positive_pd = pd.read_csv('pos_imdb_dataset.csv')
negative_pd = pd.read_csv('neg_imdb_dataset.csv')
positive_data_set = positive_pd["review"].values.tolist()
negative_data_set = negative_pd["review"].values.tolist()
# positive_data_set = twitter_samples.strings('positive_tweets.json')
# negative_data_set = twitter_samples.strings('negative_tweets.json')

predictions = []
test_pos = positive_data_set[int(len(positive_data_set) * 0.8):]
train_pos = positive_data_set[:int(len(positive_data_set) * 0.8)]
test_neg = negative_data_set[int(len(negative_data_set) * 0.8):]
train_neg = negative_data_set[:int(len(negative_data_set) * 0.8)]

train_x = train_pos + train_neg 
test_x = test_pos + test_neg

train_y = np.append(np.ones(len(train_pos)), np.zeros(len(train_neg)))
test_y = np.append(np.ones(len(test_pos)), np.zeros(len(test_neg)))





freqs = count_freqs({}, train_x, train_y)


loglikelihood={}
logprior=0

vocab = set([pair[0] for pair in freqs.keys()])
V = len(vocab)
print(V)
N_pos = N_neg=0
for pair in freqs.keys():
    if pair[1]>0:
        N_pos+=freqs[pair]
    else:
        N_neg +=freqs[pair]
print(N_pos, N_neg)
D=len(train_y)

D_pos=(len(list(filter(lambda x: x > 0, train_y))))
D_neg = (len(list(filter(lambda x: x <= 0, train_y))))
logprior = np.log(D_pos) - np.log(D_neg)

for word in vocab:
    freq_pos = lookup(freqs, word, 1)

    freq_neg = lookup(freqs, word, 0)
    p_w_pos = (freq_pos+1)/(N_pos+V)
    p_w_neg = (freq_neg + 1) / (N_neg + V)
    loglikelihood[word] = np.log(p_w_pos/p_w_neg)
    
pickle.dump(logprior, open("logprior_imdb.pkl", 'wb'))
pickle.dump(loglikelihood, open("loglikelihood_imdb.pkl", 'wb'))
