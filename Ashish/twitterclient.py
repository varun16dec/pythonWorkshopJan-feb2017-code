import sys
from tweepy import API
from tweepy import OAuthHandler
import json
 
def getTwitterAuth():
        """setup Twiiter authentication
	Return tweepy.OAuthHandler Object"""

try:
   with open("password.json","r")as file:
   	data=json.load(file)
	
except Exception as e:
     sys.stderr.write("error in json file \")
else:
     auth=OAuthHandler(data['CONSUMER_KEY',data['CONSUMER_SECRET']
