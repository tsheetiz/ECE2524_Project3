# Tweepy library to access tweets
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor

# Libraries for time, system arguments
import time, sys
from datetime import datetime, date, time, timedelta
from collections import Counter

# Import keys from keys.py
import keys

# Profanity library that detects profanity
from profanity import profanity

# Authenticate
auth = OAuthHandler(keys.TWITTER_KEY, keys.TWITTER_SECRET_KEY)
auth.set_access_token(keys.TWITTER_ACCESS_TOKEN, keys.TWITTER_ACCESS_TOKEN_SECRET)

# Create API Object
api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

account_list = []

if(len(sys.argv) > 1):
	account_list = sys.argv[1:]
else:
	print("Add usernames to the end of the commandline")
	sys.exit(0)

if len(account_list) > 0:
	for target in account_list:
		print("Getting data for " + target)
		item = api.get_user(target)
		print("name: " + item.name)
		print("screen_name: " + item.screen_name)
		print("description: " + item.description)
		print("statuses_count: " + str(item.statuses_count))
		print("friends_count: " + str(item.friends_count))
		print("followers_count: " + str(item.followers_count))

# Need to obtain the create date of the twitter account
tweets = item.statuses_count
account_created_date = item.created_at
delta = datetime.utcnow() - account_created_date
account_age_days = delta.days
print("Account age (in days): " + str(account_age_days))

if account_age_days > 0:
	print("Average tweets per day: " + "%.2f"%(float(tweets)/float(account_age_days)))

hashtags = []
mentions = []
tweet_count = 0
end_date = datetime.utcnow() - timedelta(days=30) # Break out of loop once we hit tweets older than 30 days
for status in Cursor(api.user_timeline, id=target).items():
	tweet_count += 1
	if hasattr(status, "entities"):
		entities = status.entities
		if "hashtags" in entities:
			for ent in entities["hashtags"]:
				if ent is not None:
					if "text" in ent:
						hashtag = ent["text"]
						if hashtag is not None:
							hashtags.append(hashtag)
		if "user_mentions" in entities:
			for ent in entities["user_mentions"]:
				if ent is not None:
					if "screen_name" is ent:
						name = ent["screen_name"]
						if name is not None:
							mentions.append(name)
		if status.created_at < end_date:
			break




