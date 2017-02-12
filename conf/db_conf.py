from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db_name = 'crossbone'
db = client[db_name]
db.authenticate(name="crossbone", password="crossbone")

collection_game_stats = db['game_stats']