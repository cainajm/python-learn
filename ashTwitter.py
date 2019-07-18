import pandas as pd
import tweepy
import jsonpickle

import twitter_credentials as tw

#Setup do acesso a API
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(tw.CONSUMER_KEY, tw.CONSUMER_SECRET)
    auth.set_access_token(tw.ACCESS_TOKEN, tw.ACCESS_SECRET)

    api = tweepy.API(auth)
    return api

#Cria o objeto da API
api = connect_to_twitter_OAuth()

def get_save_tweets(filepath, api, query, max_tweets=1000000, lang='pt'):

    tweetCount = 0

    #Abre o arquivo e salva os tweets
    with open(filepath, 'w') as f:

        #Executa a chamada na api com a query
        for tweet in tweepy.Cursor(api.search, q=query, lang=lang).items(max_tweets):

            #Converte para formato JSON
            f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
            tweetCount += 1

        #Mostra quantos tweets foram baixados
        print("Baixados {0} tweets".format(tweetCount))
