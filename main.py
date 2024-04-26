from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['test']

collection = db.users

documents = collection.find()
for document in documents:
    print(document)

client.close()