# GATHERING & ANALYZING INFO	10 

 1.1 Introduction								 
1.2 	purpose									 
1.3	scope										  
1.4	definitions, acronyms and abbreviations 
1.5	Project requirements						 
1.5.1 Functional Requirements 
1.5.2 Non-Functional Requirements  

### Introduction 

 

Sentiment analysis is a natural language processing technique used to identify the sentiment of data as positive or negative. It is commonly used in social media analysis, market research, and customer service. 

This project aims to develop a real-time sentiment analysis system for Reddit. The system will use machine learning algorithms to analyze the sentiment of textual data obtained from Reddit 

 
 

 

### Purpose 

The goal of this project is to develop a real-time sentiment analysis system that utilizes machine learning algorithms to analyze the sentiment of textual data obtained from reddit. The system will provide a user-friendly interface to visualize sentiment trends, sentiment distribution, and other relevant analytics. 

 

 

### Scope 

It is commonly used in social media analysis, market research, and customer service. 

 

### Definitions, Acronyms and abbreviations 

	 

 

### Project requirements 

 

#### Functional requirements 

1. The system should be able to collect data from reddit API. 

2. The system should be able to stream real time data using kafka. 

3. The system should be able to clean and preprocess data for sentiment analysis. 

4. The system should be trained using a machine learning algorithm from scratch. (naïve bayes) 

5. The system should be able to predict the score of incoming reddit posts. 

6. The system should be able to store the predicted scores along with their post title, id, date, text and scores on mongo db. 

7. The system should be able to fetch the predicted scores and visualize the results using charts on a scale of positive to negative. 

8. The system must provide a user-friendly webiste to visualize the results of sentiment analysis using chart.js . 

9. The website should be integrated with python backend server to provide real time data. 

 

 

 

#### Non-functional requirements 

1. Accuracy: The app must be able to accurately determine the sentiment of text, both positive and negative. 

2. Reliability: The app must be reliable and consistent in its results. 

3. Scalability: The app must be able to handle a large volume of text data without sacrificing accuracy or performance. 

4. Security: The app must be secure and protect the privacy of users' data. 

5. Performance: The app must be able to respond to user requests in real time. 

6. Usability: The app must be easy to use and understand. 

7. Extensibility: The app must be extensible so that new features can be added easily. 