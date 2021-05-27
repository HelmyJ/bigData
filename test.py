import tweepy
from pymongo import MongoClient

cluster = MongoClient("mongodb://nicolas:1234@cluster0-shard-00-00.ldbmg.mongodb.net:27017,cluster0-shard-00-01.ldbmg.mongodb.net:27017,cluster0-shard-00-02.ldbmg.mongodb.net:27017/test?ssl=true&replicaSet=atlas-hlqkye-shard-0&authSource=admin&retryWrites=true&w=majority")
db = cluster["test"]
collection = db["tweetBFM"]

consumer_key = "U716U9OsAgODHInhOn6fVm3QF"
consumer_secret = "U9bypaS6XbvF0HzWVKFrsdQLyrryULvj1IfGXa2erRjujne0db"
access_token = "516609771-pYtQT0lfEXHj23vaeiTUFQs0YlUjs8XY9HFyDUEi"
access_token_secret = "h7de0MRmSUCwVSX4wG68L15dZjcGSz9iIEnuBhJpYMwk7"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
cursor = tweepy.Cursor(api.user_timeline, id='bfmtv', tweet_mode="extended").items(1)

for i in cursor:
    print(i._json)
    collection.insert_one(i._json)
