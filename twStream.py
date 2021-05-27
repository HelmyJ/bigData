import json

from pymongo import MongoClient
import tweepy

cluster = MongoClient("mongodb://nicolas:1234@cluster0-shard-00-00.ldbmg.mongodb.net:27017,cluster0-shard-00-01.ldbmg.mongodb.net:27017,cluster0-shard-00-02.ldbmg.mongodb.net:27017/test?ssl=true&replicaSet=atlas-hlqkye-shard-0&authSource=admin&retryWrites=true&w=majority")
db = cluster["test"]
collection = db["tweetBFMLive"]

class TwitterListener(tweepy.StreamListener):
    def on_data(self, raw_data):
        transform = json.loads(raw_data)
        self.process_data(raw_data)

        collection.insert_one(transform)

        return True

    def process_data(self, raw_data):
        print(raw_data)


    def on_error(self, status_code):
        if status_code == 420:
            return False

class TwitterStream:


    def __init__(self, auth, listener):
        self.stream = tweepy.Stream(auth=auth, listener=listener)

    def start(self):
        self.stream.filter(track=['bfm'])
        print("ok")


if __name__ == "__main__":
    consumer_key = "U716U9OsAgODHInhOn6fVm3QF"
    consumer_secret = "U9bypaS6XbvF0HzWVKFrsdQLyrryULvj1IfGXa2erRjujne0db"
    access_token = "516609771-pYtQT0lfEXHj23vaeiTUFQs0YlUjs8XY9HFyDUEi"
    access_token_secret = "h7de0MRmSUCwVSX4wG68L15dZjcGSz9iIEnuBhJpYMwk7"

    listener = TwitterListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = TwitterStream(auth, listener)
    stream.start()
