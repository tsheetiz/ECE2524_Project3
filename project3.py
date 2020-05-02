import tweepy
import time, sys
import keys

# Authenticate
auth = tweepy.OAuthHandler(keys.TWITTER_KEY, keys.TWITTER_SECRET_KEY)
auth.set_access_token(keys.TWITTER_ACCESS_TOKEN, keys.TWITTER_ACCESS_TOKEN_SECRET)

# Create API Object
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
