import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb://nicolas:1234@cluster0-shard-00-00.ldbmg.mongodb.net:27017,cluster0-shard-00-01.ldbmg.mongodb.net:27017,cluster0-shard-00-02.ldbmg.mongodb.net:27017/test?ssl=true&replicaSet=atlas-hlqkye-shard-0&authSource=admin&retryWrites=true&w=majority")
db = cluster["test"]
collection = db["tweetBFM"]

collection.insert_one({"_id": 1, "Test": "Test"})
