import os
from dotenv import load_dotenv
from pymongo import MongoClient, ASCENDING

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))

database = client["CitiBankingSystem"]

customer_collection = database["Customers"]

user_collection = database["Users"]

# Enforce unique usernames
try:
    user_collection.create_index([("username", ASCENDING)], unique=True)
    customer_collection.create_index(
        [("username", ASCENDING)],
        unique=True,
        sparse=True  # allows documents without a username field
    )
except Exception:
    pass  # index already exists or collection has conflicts

# Back-fill username onto customer records that were created before the username field was added
for doc in customer_collection.find({"username": {"$exists": False}, "name": {"$exists": True}}):
    customer_collection.update_one(
        {"_id": doc["_id"]},
        {"$set": {"username": doc["name"]}}
    )