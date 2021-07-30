'''
@Author: Santanu Mohapatra
@Date: 30/07/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 16:00 PM
@Title: Program to create a API connection to perform twitter sentiment analysis using pyspark
'''

import logging
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import socket
import json
import os


#keys and tokens from the Twitter Dev Console
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_KEY')
access_secret = os.getenv('ACCESS_SECRET')

class TweetsListener(StreamListener):
  # tweet object listens for the tweets
  def __init__(self, csocket):
    self.client_socket = csocket
  def on_data(self, data):
    try:  
      msg = json.loads( data )
      logging.info("new message")
      # if tweet is longer than 140 characters
      if "extended_tweet" in msg:
        # add at the end of each tweet "t_end" 
        self.client_socket\
            .send(str(msg['extended_tweet']['full_text']+"t_end")\
            .encode('utf-8'))         
        logging.info(msg['extended_tweet']['full_text'])
      else:
        # add at the end of each tweet "t_end" 
        self.client_socket\
            .send(str(msg['text']+"t_end")\
            .encode('utf-8'))
        logging.info(msg['text'])
      return True
    except BaseException as e:
        logging.info("Error on_data: %s" % str(e))
    return True
  def on_error(self, status):
    logging.info(status)
    return True

  def sendData(c_socket, keyword):
    logging.info('start sending data from Twitter to socket')
    # authentication based on the credentials
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    # start sending data from the Streaming API 
    twitter_stream = Stream(auth, TweetsListener(c_socket))
    twitter_stream.filter(track = keyword, languages=["en"])

if __name__ == "__main__":
    # server (local machine) creates listening socket
    tweets = TweetsListener(StreamListener)
    s = socket.socket()
    host = "0.0.0.0"    
    port = 5555
    s.bind((host, port))
    logging.info('socket is ready')
    # server (local machine) listens for connections
    s.listen(4)
    logging.info('socket is listening')
    # return the socket and the address on the other side of the connection (client side)
    c_socket, addr = s.accept()
    print("Received request from: " + str(addr))
    # select here the keyword for the tweet data
    tweets.sendData(c_socket, keyword = ['piano'])