import sys
from tweeepy import API
from tweepy import OAuthHandler
import jason

def getTwitterAuth():
		"""setup  Twitter authentication
		Return tweepy.OAuthHandler Object"""

	try:
		with open("password.json","r")as file
			data=json.load(file)

	except Exception as e:
		sys.stderr.writer("error in json file\")
	else:
		auth=OAuthHandler(data['CONSUMER_KEY'],DATA['CONSUMER_SCRET'])
		return auth

def getTwitterClient():

	auth=getTwitterAuth()
	client=API(auth)
	return client
