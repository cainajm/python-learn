import ashTwitter as ash

query = '#Itau'

#Get those tweets
ash.get_save_tweets('tweets.json', ash.api, query)