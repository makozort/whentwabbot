import tweepy
from datetime import datetime, timedelta
import json

# created by Jack Matthews/ @makozort
# feel free to use the code anywhere but please credit me

with open("/keys.json", 'r') as f:
  data = json.load(f)                   # read in a json
  consumer_key = data["consumerkey"]
  consumer_secret = data["consumersecret"]
  access_token = data["access_token"]
  access_secret = data["accesssecret"]
  bearer_token = data["bearertoken"]

client = tweepy.Client( 
    consumer_key = consumer_key,
    consumer_secret = consumer_secret,
    access_token = access_token,               # pass variables into something the client class can use
    access_token_secret = access_secret,
    bearer_token = bearer_token
)


query = 'from:Bungie has:links' # check recent (7 days) tweets from our user that contain links
tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=10)
substring = "This week at Bungie," 
for tweet in tweets.data:
    if  substring in tweet.text: # only grab the id
        id = tweet.id
        with open("tweets.txt", 'r') as f:
            for tweetid in f:
                if (tweetid.rstrip("\n")) == str(id): # this loop here checks our list to see if it has already been retweeted, if so, it wont continue
                    print("tweet already done")
                    exit()
                
tweetdate = (tweet.created_at)
client.create_tweet(text="Where TWAB? TWAB here:", quote_tweet_id=id)       
with open("tweets.txt", 'a') as f:
    f.write(str(id)+"\n") # write this tweets id to a file so they bot does not tweet it over and over
    with open("twab.txt", 'w') as f: # overwrite last weeks twab TODO: add backlogs sorted by date
        f.write("https://twitter.com/twitter/statuses/"+(str(id).rstrip("\n")))
    import twabnow
    twabnow()


