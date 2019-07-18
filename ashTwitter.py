import pandas as pd
import tweepy
import jsonpickle

import twitter_credentials as tw

#Setup access API
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(tw.CONSUMER_KEY, tw.CONSUMER_SECRET)
    auth.set_access_token(tw.ACCESS_TOKEN, tw.ACCESS_SECRET)

    api = tweepy.API(auth)
    return api

# Create API object
api = connect_to_twitter_OAuth()

def get_save_tweets(filepath, api, query, max_tweets=1000000, lang='pt'):

    tweetCount = 0

    #Open file and save tweets
    with open(filepath, 'w') as f:

        #Send the query
        for tweet in tweepy.Cursor(api.search, q=query, lang=lang).items(max_tweets):

            #Convert to JSON format
            f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
            tweetCount += 1

        #Display how many tweets we habe collected
        print("Downloaded {0} tweets".format(tweetCount))