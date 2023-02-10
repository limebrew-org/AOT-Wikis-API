from api.constants import MONGO_INITDB_DATABASE, AOT_WIKI_DB_CONNECTION_URL
from pymongo import MongoClient

def createConnection():
    aotWikiClient = MongoClient(AOT_WIKI_DB_CONNECTION_URL)
    return aotWikiClient,MONGO_INITDB_DATABASE

