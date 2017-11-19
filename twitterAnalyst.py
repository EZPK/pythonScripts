import tweepy
from textblob import TextBlob

consumer_key = 'secret'
consumer_secret = 'encore plus secret'

acces_token = 'terriblement secret'
acces_token_secret = 'OMG classified files for sure'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acces_token, acces_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    #print(tweet.text)
    print('Longueur de public tweets:' + str(len(public_tweets)))
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
