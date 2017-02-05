import sys
from tweepy import API
from tweepy import OAuthHandler
import json

def getTwitterAuth():
	"""Setup twitter authentication.
	Return : tweepy.OAuthHandler object
	"""
	try:
		with open("credentials.json","r") as file:
			credentials=json.load(file)
		consumerKey=credentials['TWITTER_CONSUMER_KEY']
		consumerSecret=credentials['TWITTER_CONSUMER_SECRET']
		accessToken=credentials['TWITTER_ACCESS_TOKEN']
		accessSecret=credentials['TWITTER_ACCESS_SECRET']
	except KeyError:
		sys.stderr.write("file reading error\n")
		sys.exit(1)
	finally:
		auth=OAuthHandler(consumerKey,consumerSecret)
		auth.set_access_token(accessToken,accessSecret)
		return auth
def getTwitterClient():
	"""Setup Twitter API client.
	Return : tweepy.API object"""
	auth = getTwitterAuth()
	client=API(auth)
	return client
