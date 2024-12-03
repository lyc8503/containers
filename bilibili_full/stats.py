from pymongo import MongoClient


with MongoClient("mongodb://localhost:27017/") as client:
    collection = client['bili']['meta']
    result = collection.find().sort({"data.stat.view": -1}).limit(100)
    for doc in result:
        print(f"av{doc['_id']} {doc['data']['title']} {doc['data']['stat']['view']}/{doc['data']['stat']['coin']}")
