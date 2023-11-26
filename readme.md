# Reddit Real time sentiment analysis dashboard



Getting Started
To get started, you will need to install the following dependencies:
```
Kafka
Python 3
confluent_kafka==2.2.0
nltk==3.8.1
numpy==1.26.0
pandas==2.1.1
praw==7.7.1
pymongo==4.5.0
python-dotenv==1.0.0
scikit_learn==1.3.1

```

run pip install requirements.txt for installing dependencies.


Once you have installed the dependencies, you can download and start the Kafka environment by running the following commands:


## STEP 1: GET KAFKA
Download the latest Kafka release and extract it:

$ tar -xzf kafka_2.13-3.5.0.tgz
$ cd kafka_2.13-3.5.0

## STEP 2: START THE KAFKA ENVIRONMENT
NOTE: Your local environment must have Java 8+ installed.


Kafka with ZooKeeper
Run the following commands in order to start all services in the correct order:

## Start the ZooKeeper service
$ bin/zookeeper-server-start.sh config/zookeeper.properties
Open another terminal session and run:

### Start the Kafka broker service
$ bin/kafka-server-start.sh config/server.properties


After setting the environment  run kafka-reddit and consumer.py


### Training Naive bayes model for sentiment analysi

Download a training dataset for sentiment analysis. I have  used imdb 50k movie reviews.
Develop the vocab of dataset
Calculate log priors for dataset and log likelihood of each word in the dataset.
dump the log prior and log likelihood in pickle file for future use.

### Data retrieval

Search for a subreddit to get it's recent submissions.

### Data preprocessing

Use natural language processing techniques to clean the data. 

### Predicting scores

call predict_score function to calculate the score

### Data storage in mongodb

store the predicted scores in mongodb

### Data visualization

Generate a bar chart and a posts tab for data visualization

### Data collection and Sentiment analysis


