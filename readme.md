# Final Project Prototype

This repository contains the prototype for my final project, which is a real-time sentiment analysis system. The system uses Kafka to stream textual data from Reddit, and then uses natural language processing (NLP) techniques and machine learning algorithms to analyze the sentiment of the data. T

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


STEP 1: GET KAFKA
Download the latest Kafka release and extract it:

$ tar -xzf kafka_2.13-3.5.0.tgz
$ cd kafka_2.13-3.5.0

STEP 2: START THE KAFKA ENVIRONMENT
NOTE: Your local environment must have Java 8+ installed.


Kafka with ZooKeeper
Run the following commands in order to start all services in the correct order:

# Start the ZooKeeper service
$ bin/zookeeper-server-start.sh config/zookeeper.properties
Open another terminal session and run:

# Start the Kafka broker service
$ bin/kafka-server-start.sh config/server.properties


After setting the environment 

run kafka-reddit and consumer.py



1. Data Collection:
   - Integrate with reddit API to collect real-time textual data for sentiment analysis.
```
      Use praw library to connect to reddit API
         reddit = praw.Reddit(
                  client_id=CLIENT_ID,
                 client_secret=CLIENT_SECRET,
                 password=PASSWORD, 
                 user_agent=USER_AGENT,
                 username=USERNAME,)
         for submission in reddit.subreddit("bitcoin").stream.submissions():
             if submission.selftext is not empty
              then 
                    add it to list
               after the posts list is complete send it to the producer
               

```



   - Develop a data retrieval mechanism using Python to fetch and store the data.
        - use kafka to store incoming data temporarily 
        -    from the posts list send each post to the producer


        - receive incoming data using kafka consumer
        ```
         while True:
                     msg = consumer.poll(1.0)
                     if msg is None:
                         continue
                     if msg.error():
                         print("Consumer error: {}".format(msg.error()))
                         continue     
        ```
                   
 
2. Sentiment Analysis:
   - Apply natural language processing techniques to preprocess and analyze the collected textual data.
```
         def clean_text(text):
             text = text.lower() # lower case
             text = re.sub(r'[^\w\s]', '', text) #remove punctuation marks
             text = re.sub(" +", " ", text) # remove multiple spaces
             text = re.sub(r'http\S+', '', text, flags=re.MULTILINE) # remove links
             stop_words = set(stopwords.words('english')) # remove stopwords
             text = ' '.join([word for word in text.split() if word not in stop_words])
             return text

```

   - Utilize machine learning algorithms to train a sentiment analysis model for accurate sentiment classification.
        - implement naive bayes from scratch to train sentiment analysis 


important note:
The collected data is stored in reddit_posts_analysis.json