import pandas as pd
import tweepy
import jsonpickle

import ashTwitter as ash

def tweets_to_df(path):
    
    # Aqui é onde abrimos o arquivo já gerado pelo primeiro passo de captura
    tweets = list(open(path, 'rt'))
    
    text = []
    date = []
    favorite = []
    retweet = []
    follower = []
    following = []
    user = []
    screen_name = []

    for t in tweets:
        t = jsonpickle.decode(t)
        
        # Texto
        text.append(t['text'])
        
        # Data
        date.append(t['created_at'])
            
        # Numero de favoritos
        favorite.append(t['favorite_count'])       
        
        # Contador de retweets
        retweet.append(t['retweet_count'])
        
        # Numero de followers
        follower.append(t['user']['followers_count'])
        
        # Numero de following
        following.append(t['user']['friends_count'])
        
        # Nome do usuario
        user.append(t['user']['name'])

        # Id do usuario
        screen_name.append(t['user']['screen_name'])
        
    # Valores das colunas
    d = {'texto': text,
         'data' : date,
         'favoritos': favorite,
         'retweet': retweet,
         'followers': follower,
         'following' : following,
         'user': user,
         'id' : screen_name
        }
    
    return pd.DataFrame(data = d)