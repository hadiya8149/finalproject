The goal of this project is to develop a real-time sentiment analysis system that utilizes natural language processing techniques and machine learning algorithms to analyze the sentiment of textual data obtained from reddit. The system will provide a user-friendly interface to visualize sentiment trends, sentiment distribution, and other relevant analytics.



1. Data Collection:
   - Integrate with reddit API to collect real-time textual data for sentiment analysis.
        - Use praw library to connect to reddit API
        - reddit = praw.Reddit(
                 client_id="RYwplqMp-ThgglPOj6-ZTQ",
                client_secret="rKC3QsYyR9E9XsMY7nAO8v5A_cvYfg",
                password="TVsA/ZRHE2gEM7A", 
                user_agent="rsa dashboard by u/LiteratureChemical50",
                username="LiteratureChemical50",)
        - for submission in reddit.subreddit("bitcoin").hot(limit=1000):
            if submission.selftext == "":
                continue
            posts.append({
                "title": submission.title,
                "text": submission.selftext,
                "url": submission.url
            })
        -



   - Develop a data retrieval mechanism using Python to fetch and store the data.
        - use kafka to store incoming data temporarily 
            for post in posts:
                producer.poll(0)
                producer.produce('testevent', str(post).encode('utf-8'), callback=delivery_report)
            
            producer.flush()


        - receive incoming data using kafka consumer
                while True:
                    msg = consumer.poll(1.0)
                    if msg is None:
                        continue
                    if msg.error():
                        print("Consumer error: {}".format(msg.error()))
                        continue        
 
2. Sentiment Analysis:
   - Apply natural language processing techniques to preprocess and analyze the collected textual data.
        def clean_text(text):
            text = text.lower() # lower case
            text = re.sub(r'[^\w\s]', '', text) #remove punctuation marks
            text = re.sub(" +", " ", text) # remove multiple spaces
            text = re.sub(r'http\S+', '', text, flags=re.MULTILINE) # remove links
            stop_words = set(stopwords.words('english')) # remove stopwords
            text = ' '.join([word for word in text.split() if word not in stop_words])
            return text



   - Utilize machine learning algorithms to train a sentiment analysis model for accurate sentiment classification.
        -implement naive bayes from scratch to train sentiment analysis 