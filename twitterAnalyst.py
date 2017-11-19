import tweepy
from textblob import TextBlob

consumer_key = 'i9AA2Bel71Ls2gAwgRnvVdVyg'
consumer_secret = 'mVSIAJ6sye0EYUp5itwCQEvP0yH75v0DXN5oM6f3H50KvmvDKQ'

acces_token = '1251785250-bM0wi2GnCOIcqHHbKz0XCwiTZNO3vtRMpSq34rh'
acces_token_secret = 'VK89GhtMpNCm5b6NY1fgVmT7en7kd2qFS47vMtq2ZIpfp'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(acces_token, acces_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    #print(tweet.text)
    print('Longueur de public tweets:' + str(len(public_tweets)))
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
