from pymongo import MongoClient
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import ast
import json

dbconn = MongoClient()
db = dbconn.collections
dataset = db.ladygaga


access_token='714281447046168576-OU13L4qpq2tRqOnoA75YcKjn6jr1vGr'
access_token_secret='IpcQj98w8XGe3BGWKnMacLoMEQBenTeNr6af75iKWaCW2'
consumer_key='W1Tw4ZcNKEB0dTw7RWBLJRUQ4'
consumer_secret='8q2T0bmnMk68C9UJUJukcBEHEaHpuCY2iFNEP58A16iCVGXkjc'


class StdOutListener(StreamListener):

    def __init__(self,time_limit=10):
        self.time = time.time()
        self.limit = time_limit
        print('initialized')

    def on_data(self,data):
#        while (time.time() -self.time) < self.limit:
        payload = json.loads(data)
        print('Text:',payload['text'])
        print('ID:',payload['user']['id_str'])
            #dataset.insert({'id': data['user']['id_str'],'text':data['text']})
#except BaseException as e:
 #               print('Failed ondata,',str(e))
  #              time.sleep(5)
   #             pass

        return True

    def on_error(self,status):
        print(status)

if __name__ == '__main__':
    #connect to streaming api
    l = StdOutListener()
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    stream = Stream(auth,l)

    #search your query
    query = []
    answer = 'n'
    while answer != 'y':
        query = input("Enter tokens separated by spaces: ")
        print(query.split(' '))
        answer = input("Happy with those? Type y: ")
    
    stream.filter(track=query.split(' '))
