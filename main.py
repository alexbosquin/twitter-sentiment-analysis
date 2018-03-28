import tweepy
import pandas as pd
from textblob import TextBlob

#those keys are fake so make your own twitter API
consumer_key = "nwO8OwLnoBjfU54686412woobzW2mjwHz"
consumer_secret = "Ad5XOISf3jsk3NKdZpW1dNy02ToitwrG7UByf12313456g7glaFk88ccJb"
access_token = "969882002991304704-dg5blh0eQRO89789456oLcPdGpBbWafNAiIo7F8"
access_token_secret = "hxroMSIB5KDsNpzuAQ8Nbn9cW2cC52v54678945aWVYdDFRU9UEa7"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler=auth)

def get_sentiments(hashtag):
    public_tweets = api.search(hashtag)
    info_list = ([],[])
    array_tweets = []
    array_sentiments = []
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        array_tweets.append(tweet.text)
        array_sentiments.append(str(analysis.sentiment))
    return array_tweets, array_sentiments

columns = ["tweet", "sentiment"]
tweets, sentiments = get_sentiments('godotengine')

df = pd.DataFrame([tweets, sentiments], columns)
df.to_csv("tweets_sentiments.csv", sep='\t', encoding='utf-8')

print('done')



