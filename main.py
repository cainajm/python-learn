import ashTwitter as ash
import ashTwitterToCsv as csv

# Montamos a query conforme o que necessitamos para buscar pela api do Twitter
query = '#Itau'

# Metodo responsavel por fazer a captura atraves da api do Twitter
ash.get_save_tweets('tweets.json', ash.api, query)

# Metodo responsavel por transformar todos os tweets que estão em formato json para um csv e depois persistir em um S3
tweets_df = csv.tweets_to_df('tweets.json')
tweets_df.to_csv("teste.csv")