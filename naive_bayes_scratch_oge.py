import pandas as pd
import numpy as np
import string
from utils import lookup, process_tweet
import nltk
from nltk.corpus import stopwords, twitter_samples
from sklearn.preprocessing import MinMaxScaler

# pos_data = pd.read_csv("positive_dataset.csv")
# neg_data = pd.read_csv("neg_dataset.csv")
all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')

# all_positive_tweets = pos_data["text"].values.tolist()
# all_negative_tweets = neg_data["text"].values.tolist()




test_pos = all_positive_tweets[int(len(all_positive_tweets) * 0.8):]
train_pos = all_positive_tweets[:int(len(all_positive_tweets) * 0.8)]
test_neg = all_negative_tweets[int(len(all_negative_tweets) * 0.8):]
train_neg = all_negative_tweets[:int(len(all_negative_tweets) * 0.8)]
print(len(train_pos))
train_x = train_pos + train_neg 
test_x = test_pos + test_neg

train_y = np.append(np.ones(len(train_pos)), np.zeros(len(train_neg)))
test_y = np.append(np.ones(len(test_pos)), np.zeros(len(test_neg)))


def count_tweets(result, tweets, ys):
    '''
    Input:
        result: a dictionary that will be used to map each pair to its frequency
        tweets: a list of tweets
        ys: a list corresponding to the sentiment of each tweet (either 0 or 1)
    Output:
        result: a dictionary mapping each pair to its frequency
    '''

    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###
    for y, tweet in zip(ys, tweets):
        for word in process_tweet(tweet):
            # define the key, which is the word and label tuple
            pair = (word,y)

            # if the key exists in the dictionary, increment the count
            if pair in result:
                result[pair] += 1

            # else, if the key is new, add it to the dictionary and set the count to 1
            else:
                result[pair] = 1
    ### END CODE HERE ###

    return result

result={}
tweets=[]
freqs = count_tweets({}, train_x, train_y)
def train_naive_bayes(freqs, train_x, train_y):
    loglikelihood={}
    logprior=0

    vocab = set([pair[0] for pair in freqs.keys()])
    V = len(vocab)

    N_pos = N_neg=0
    for pair in freqs.keys():
        if pair[1]>0:
            N_pos+=freqs[pair]
        else:
            N_neg +=freqs[pair]

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
    return logprior, loglikelihood
    
logprior, loglikelihood = train_naive_bayes(freqs, train_x, train_y)
def naive_bayes_predict(tweet, logprior, loglikelihood):
    '''
    Input:
        tweet: a string
        logprior: a number
        loglikelihood: a dictionary of words mapping to numbers
    Output:
        p: the sum of all the logliklihoods of each word in the tweet (if found in the dictionary) + logprior (a number)

    '''
    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###
    # process the tweet to get a list of words
    word_l = process_tweet(tweet)

    # initialize probability to zero
    p = 0

    # add the logprior
    p += logprior

    for word in word_l:

        # check if the word exists in the loglikelihood dictionary
        if word in loglikelihood:
            # add the log likelihood of that word to the probability
            p += loglikelihood[word]

    ### END CODE HERE ###
    
    return p


def test_naive_bayes(test_x, test_y, logprior, loglikelihood):
    """
#     Input:
#         test_x: A list of tweets
#         test_y: the corresponding labels for the list of tweets
#         logprior: the logprior
#         loglikelihood: a dictionary with the loglikelihoods for each word
#     Output:
#         accuracy: (# of tweets classified correctly)/(total # of tweets)
"""
    accuracy = 0  # return this properly

    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###
    y_hats = []
    for tweet in test_x:
        # if the prediction is > 0
        if naive_bayes_predict(tweet, logprior, loglikelihood) > 0:
            # the predicted class is 1
            y_hat_i = 1
        else:
            # otherwise the predicted class is 0
            y_hat_i = 0

        # append the predicted class to the list y_hats
        y_hats.append(y_hat_i)

    # error is the average of the absolute values of the differences between y_hats and test_y
    error = np.mean(np.absolute(y_hats-test_y))
    print("error is ", error)
    # Accuracy is 1 minus the error
    accuracy = 1-error

    ### END CODE HERE ###

    return accuracy
accuracy = test_naive_bayes(test_x, test_y, logprior, loglikelihood)
print("Naive Bayes accuracy = %0.4f" %(accuracy))

# if score is greater than 0 then it is positive if smaller than 0 then negative

def calculate_confusion_matrix(predicted_labels, actual_labels):
  """
  Calculates the confusion matrix for a classification model.

  Args:
    predicted_labels: A numpy array of the predicted labels.
    actual_labels: A numpy array of the actual labels.

  Returns:
    A numpy array of the confusion matrix.
  """

  confusion_matrix = np.zeros((2, 2))
  actual_labels = actual_labels.astype(int)
  for i in range(len(predicted_labels)):
    confusion_matrix[predicted_labels[i], actual_labels[i]] += 1
  return confusion_matrix

# Make predictions on the test set

predicted_labels = []
predictions = []
for tweet in test_x:
  ans = naive_bayes_predict(tweet, logprior, loglikelihood)
  if ans>0:
      predicted_labels.append(1)
  else:
      predicted_labels.append(0)
  predictions.append(ans)

confusion_matrix = calculate_confusion_matrix(predicted_labels, test_y)



def calculate_metrices(confusion_matrix, predicted_labels, actual_labels):
    metrices = {}
    actual_labels = actual_labels.astype(int)
    TP=confusion_matrix[0][0]
    print(TP)
    FP=confusion_matrix[0][1]
    print(FP)
    FN = confusion_matrix[1][0]
    print(FN)
    precision = TP/(TP+FP)
    recall = TP/(TP+FN)
    f1_score = 2*(precision*recall)/(precision+recall)
    mse = np.square(np.subtract(test_y, predicted_labels)).mean()
    
    po = np.sum(predicted_labels == actual_labels) / len(predicted_labels)

  # Calculate the expected proportion of agreement by chance
    pe = np.sum(np.prod(np.bincount(predicted_labels, minlength=2) / len(predicted_labels)))

  # Calculate the linear kappa coefficient
    linearKappa = (po - pe) / (1 - pe)
    observed_agreement = np.sum(np.diag(confusion_matrix))/np.sum(confusion_matrix)
    expected_agreement = np.zeros((len(confusion_matrix), len(confusion_matrix)))
    for i in range(len(confusion_matrix)):
        for j in range(len(confusion_matrix)):
          expected_agreement[i, j] = np.dot(confusion_matrix[i, :], confusion_matrix[:, j]) / np.sum(confusion_matrix)**2
    
    expected_agreement = np.sum(expected_agreement) / np.sum(confusion_matrix)**2

    # Calculate the quadratic kappa score.
    quadratic_kappa = (observed_agreement - expected_agreement) / (1 - expected_agreement)
    metrices["precion"] = precision
    metrices["recall"] = recall
    metrices["f1_score"] = f1_score    
    metrices["mse"] = mse
    metrices["linear kappa"] =linearKappa
    metrices["quadratic kappa"] = quadratic_kappa
   

    return metrices







metrices = calculate_metrices(confusion_matrix, predicted_labels, test_y)
metrices["accuracy"] = accuracy
print(metrices)
print(confusion_matrix)

predictions_array = np.array(predictions)
predictions_reshaped = predictions_array.reshape(-1, 1)
predictions_reshaped = np.abs(predictions_reshaped)
scaler = MinMaxScaler()
scaler.fit_transform(predictions_reshaped)
scaled_predictions = scaler.transform(predictions_reshaped)

print(scaled_predictions)

# test_data = pd.read_csv("data_analysis3.csv")
# data = test_data["content"].values.tolist()
# scores=[]
# for i in data:
#     score = naive_bayes_predict(i, logprior,  loglikelihood)
#     scores.append(score)
# test_data["sentiment140_data_scores"] = scores
# test_data.to_csv("data_analysis.csv")
