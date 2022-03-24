import tweepy
import time

auth = tweepy.OAUTHandler("first consumer key","seret key")
auth.set_access_tocken ("","")

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_Rate_limit_notyfy=True)

user = api.me()
for follower in tweepy.cursor(api.followers).items():
    #print(follower.name)
    #if follower.name == 'ntv':
     #   follower.follow()
#print()
#search tweepy on google to find all function

search = "javascript"
nrTweets = 500

for tweets in tweepy.cursor(api.search,search).items(nrTweets):
    try:
        print("tweet liked")
        tweet.favorite()
        tweet.retweet()
        time.sleep(10)
    except tweet.TweepError as r:
        print(e.reson)
    except stopIteration:
        break