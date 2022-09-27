import tweepy
import pandas
import os
import re
from cleantext import clean


#Put your Bearer Token in the parenthesis below
def Acess_data(input_tag):
    client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAABnWfQEAAAAA6rc%2B0aC5ThIwimyqicKcGl3Gz10%3Drsh9jWZ3PF9QLhxfSp156XQEYF3WzvbtqEUe7G787Ey8ikLchV')


    # Get tweets that contain the hashtag #petday
    # -is:retweet means I don't wantretweets
    # lang:en is asking for the tweets to be in english
    query = input_tag+ ' -is:retweet lang:en'
    tweets = tweepy.Paginator(client.search_recent_tweets, query=query,
                                tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(limit=1000)
    file1=open("actual_data.txt","w")
    for tweet in tweets:
        tweet_text = (tweet.text).encode('utf-8').strip()
        t=tweet_text.decode()
        a=clean(t,no_emoji=True)
        file1.write(a)
                    #print(tweet_text)
					#tweet_text = (tweet_text.decode()).replace('\n', " ")
					
					#tweets[tweet.text] = 1  # # for duplicate identification
					
					#file1.write(tweet_text+"\n")
    #print(tweet.encode('utf-8').strip())
    #file1.write(tweet.text)
    #file1.write("\n")
    #print(type(tweet))
    #file1.write(str(tweet))
    #for i in tweet.context_annotations:
    #    print(i['domain']['description'])
        #print(i.domain.description)
    #if len(tweet.context_annotations) > 0:
    #    print(tweet.context_annotations)
    #    break
Acess_data("#Boycottbollywood")