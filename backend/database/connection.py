from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = "mongodb://localhost:27017"
client = MongoClient(MONGO_URL)
db = client["AgriSens1"]
user_collection = db["users"]

