from dotenv import dotenv_values

config = dotenv_values(".env")

MONGO_INITDB_DATABASE=config["MONGO_INITDB_DATABASE"]
AOT_WIKI_DB_CONNECTION_URL= config["AOT_WIKI_DB_CONNECTION_URL"] 
AOT_WIKI_DB_MODEL_NAME = "characters"
