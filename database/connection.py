from pymongo.mongo_client import MongoClient

client = MongoClient("mongodb+srv://admin:2d3d4d5d@cluster0.xlbm1cf.mongodb.net/?retryWrites=true&w=majority")

db = client.book_db

collection_name = db["book_collection"]

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)