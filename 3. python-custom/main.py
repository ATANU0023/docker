from pymongo import MongoClient
from pprint import pprint

MONGO_URL = "mongodb://nongo:27017"
client = MongoClient(MONGO_URL)
db = client.admin
dbs_list = db.command("ListDatabases")
pprint(dbs_list)