import pickle
from utils import *
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from model import naive_bayes_predict
from nltk.corpus import  twitter_samples

positive_data_set = twitter_samples.strings('positive_tweets.json')
negative_data_set = twitter_samples.strings('negative_tweets.json')

predictions = []
test_pos = positive_data_set[int(len(positive_data_set) * 0.8):]
test_neg = negative_data_set[int(len(negative_data_set) * 0.8):]

test_x = test_pos + test_neg

test_y = np.append(np.ones(len(test_pos)), np.zeros(len(test_neg)))


logprior = pickle.load(open('./logprior.pkl', 'rb'))
loglikelihood = pickle.load(open('./loglikelihood.pkl', 'rb'))
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

"""
The following code calculates metrices and confusion metrics on the sample tweets test data. This will be changed in the final project deliverable for the realtime data.
And I am not storing this on mongo db right now because we are not building the visualization and data analytics part right now.

"""

predicted_labels = []

for tweet in test_x:
  ans = naive_bayes_predict(tweet, logprior, loglikelihood)
  if ans>0:
      predicted_labels.append(1)
  else:
      predicted_labels.append(0)
  

confusion_matrix = calculate_confusion_matrix(predicted_labels, test_y)



def calculate_metrices(confusion_matrix, predicted_labels, actual_labels):
    metrices = {}
    actual_labels = actual_labels.astype(int)
    TP=confusion_matrix[0][0]
    FP=confusion_matrix[0][1]
    FN = confusion_matrix[1][0]
    precision = TP/(TP+FP)
    recall = TP/(TP+FN)
    f1_score = 2*(precision*recall)/(precision+recall)
    mse = np.square(np.subtract(test_y, predicted_labels)).mean()
    # calculate the observed proportion of agreement
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

# the following code scales the predictions from 0 to 1 once we have calculated all the sentiment score of posts we will scale them for visualization


# print("these are scaled predictions from 0 to 1") 
# predictions_array = np.array(predictions)
# predictions_reshaped = predictions_array.reshape(-1, 1)
# predictions_reshaped = np.abs(predictions_reshaped)
# scaler = MinMaxScaler()
# scaler.fit_transform(predictions_reshaped)
# scaled_predictions = scaler.transform(predictions_reshaped)
# print(scaled_predictions)


