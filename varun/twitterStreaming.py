import sys
import time
import json
from tweepy import Stream
from tweepy.streaming import StreamListener
from twitterClient import getTwitterAuth

class CustomListener(StreamListener):
	"""
	Custom StreamListener for streaming Twitter data
	"""
	def on_data(self,data):
		try:
			jsonData=json.loads(data)
			tweet=jsonData['text']
			print(tweet,"\n")
			
		except Exception as e:
			sys.stderr.write("Error on_data :{}\n".format(e))
			time.sleep(5)
		finally:
			return True
	
	def on_error(self,status):
		if status == 420:
			sys.stderr.write("Rate limit Exceeded\n")
			return False
		else :
			sys.stderr.write("Error {}\n".format(status))
			return True

if __name__ == '__main__':
	auth=getTwitterAuth()
	twitterStream=Stream(auth,CustomListener())
	twitterStream.filter(track=["beyonce"],async=True) #for hashTag
