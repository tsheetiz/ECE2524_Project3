from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import time, sys
from datetime import datetime, date, time, timedelta
from collections import Counter
import keys

# Authenticate
auth = OAuthHandler(keys.TWITTER_KEY, keys.TWITTER_SECRET_KEY)
auth.set_access_token(keys.TWITTER_ACCESS_TOKEN, keys.TWITTER_ACCESS_TOKEN_SECRET)

# Create API Object
api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

account_list = []

if(len(sys.argv) > 1):
	account_list = sys.argv[1:]
else:
	print("Please provide a list of usernames at the CMD.")
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

