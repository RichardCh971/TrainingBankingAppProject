import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

client = MongoClient(os.getenv("MONGODB_URI"))

database = client["CitiBankingSystem"]

customer_collection = database["Customers"]