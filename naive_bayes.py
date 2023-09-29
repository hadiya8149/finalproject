import pandas as pd
import numpy as np
import string
from utils import lookup, process_tweet
import nltk
from nltk.corpus import stopwords, twitter_samples


class Naive_Bayes_Classifier:
    def __init__(self, pos_file="pos_imdb_dataset.csv", neg_file ="neg_imdb_dataset.csv"):
        self.pos_data=pd.read_csv(pos_file)
        self.neg_data = pd.read_csv(neg_file)
        
        self.positive_text = self.pos_data["review"].values.tolist()
        self.negative_text = self.neg_data["review"].values.tolist()
    def split(self):
        self.test_pos = self.positive_text[int(len(self.positive_text) * 0.8):]
        self.train_pos = self.positive_text[:int(len(self.positive_text) * 0.8)]
        self.test_neg = self.negative_text [int(len(self.negative_text ) * 0.8):]
        self.train_neg = self.negative_text [:int(len(self.negative_text ) * 0.8)]

        self.train_x = self.train_pos + self.train_neg 
        self.test_x = self.test_pos + self.test_neg
        # avoid assumptions about the length of all_positive_tweets
        train_y = np.append(np.ones(len(self.train_pos)), np.zeros(len(self.train_neg)))
        test_y = np.append(np.ones(len(self.test_pos)), np.zeros(len(self.test_neg)))
    def count_tweets():
        
    def train_model():

    def predict_model(): # model that will be used by other programs to find the score

    def test_model():

    def calculate_matrix():

    def make_predicted_labels():

    def calculate_metrices():


if __name__ == "__main__":
    bayes_instance = Naive_Bayes_Classifier()
