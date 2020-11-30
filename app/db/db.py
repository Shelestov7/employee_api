import os
from pymongo import MongoClient

client = MongoClient(os.environ.get("DB_HOST", '127.0.0.1'), os.environ.get("DB_PORT", 27017))
db = client.employees
