import tweepy
import time, sys
import keys

class MyStreamListener(tweepy.StreamListener):
	def __init__(self, api):
		self.api = api
		self.me = api.me()
	
	def on_status(self, tweet):
		print(f"{tweet.user.name}:{tweet.text}")

	def on_error(self, status):
		print("Error Detected")

# Authenticate
auth = tweepy.OAuthHandler(keys.TWITTER_KEY, keys.TWITTER_SECRET_KEY)
auth.set_access_token(keys.TWITTER_ACCESS_TOKEN, keys.TWITTER_ACCESS_TOKEN_SECRET)

# Create API Object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Capture Tweet
tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["Python", "Django", "Tweepy"], languages=["en"])


