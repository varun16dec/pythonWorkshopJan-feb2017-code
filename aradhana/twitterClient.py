import sys 
from tweepy import API
from tweepy import OAuthHandler
import json 


def getTwitterAuth():
	"""setup Twitter authentication
	 Return tweepy.OAuthHandler Object"""
	
	try:
		with open("password.json","r") as file:
			data=json.load(file)
	except Exception as e:
		sys.stderr.write("error in json file\")
	else:
		auth=OAuthHandler(data['CONSUMER_KEY'],data['CONSUMER_SECRET]
		auth.set_access_token(data['ACCESS_TOKEN',data['ACCESS_SECRET])
		return auth
def getTwitterClient():
	auth=getTwitterAuth()
	client=API(auth)
	return client
