from dotenv import dotenv_values
import os
from api.utils import handleEnv


PYENV = os.environ.get('PYENV', '')
print("Running in {} environment".format(PYENV))
config = dotenv_values(handleEnv(PYENV))

MONGO_INITDB_DATABASE=config["MONGO_INITDB_DATABASE"]
AOT_WIKI_DB_CONNECTION_URL= config["AOT_WIKI_DB_CONNECTION_URL"] 

AOT_WIKI_DB_MODEL_NAME = "characters"
