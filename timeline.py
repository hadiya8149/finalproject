import tweepy
consumer_key = "PB9R8D8INd3awttH687Mu4ZyV"
consumer_secret = "4pspn23kvTIbgLVHJ5rdxFQYJ3RTBWZNKUzi49YR2pUv8IW8hh"
access_token= "1698285355794141184-KWhNyJHh30xTvLsyjXosz7pnRgdQYs"
access_secret = "8jFSOUqZ0tyaIDoXaDc7TVfAQw3UxJ7th941tHLSWkJhH"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 
public_tweets = api.home_timeline()
# foreach through all tweets pulled
for tweet in public_tweets:
   # printing the text stored inside the tweet object
   print (tweet.text)
   