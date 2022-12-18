from re import I
import tweepy

twitter_keys = {
    'consumer_key':         'KEYS',
    'consumer_secret':      'KEYS',
    'access_token_key':      'KEYS',
    'access_token_secret':   'KEYS'
}

auth = tweepy.OAuthHandler(twitter_keys["consumer_key"], twitter_keys["consumer_secret"])
auth.set_access_token(twitter_keys["access_token_key"], twitter_keys["access_token_secret"])

api = tweepy.API(auth)

#Faz a chamada de tweets a partir de uma data e buscando por uma palavra chave
search_words = ":( :)"
date_since = "2001-01-01"
public_tweets = api.search_tweets(q=search_words,
                                  lang="pt-br",
                                  since=date_since,
                                  cont=20)

i = 1
for tweet in public_tweets:
    print(tweet.text)
    i = i + 1

print(i)