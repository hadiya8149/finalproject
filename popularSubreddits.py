# reddit crawler
import praw
# sentiment analysis
reddit = praw.Reddit(
                 client_id="RYwplqMp-ThgglPOj6-ZTQ",
                client_secret="rKC3QsYyR9E9XsMY7nAO8v5A_cvYfg",
                password="TVsA/ZRHE2gEM7A",
                user_agent="rsa dashboard by u/LiteratureChemical50",
                username="LiteratureChemical50",)
print(reddit.user.me())
# list of topics that you are interested in 
topics =['bitcoin', 'politics', 'cryptocurrency']
# Hot new rising topics
headlines = set()
posts =[]
for submission in reddit.subreddit("bitcoin").hot(limit=None):
    # print(submission.selftext)
    if submission.selftext:
        posts.append(submission.selftext)
    else:
        print("empty")
print(len(posts))
# for submission in reddit.subreddit('bitcoin').hot(limit=None):
#  print(submission.title)#Subreddit Title
#  print(submission.id) #ID
#  print(submission.author) #Author of the subreddit
#  print(submission.created_utc) #Date and time being created
#  print(submission.score) # Average Score
#  print(submission.upvote_ratio) # Upvote ratio
#  print(submission.url) # Like to the Subreddit
    # print(submission)
 
#  headlines.add(submission.title)
# print(len(headlines))
# now add them to the mongo db
