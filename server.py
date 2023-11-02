from fastapi import FastAPI
from api.routes import AOTWikiRouter
from api.db import createConnection
import os

# Get the path to the credentials file
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

print("credentials: ",credentials_path)

app = FastAPI()

# @app.on_event("startup")
# def startup_db_connection():
#     connection,db = createConnection()   
#     app.connection = connection
#     app.db = app.connection[db]
#     print("Connected to the AOT_WIKI database!")

# @app.on_event("shutdown")
# def shutdown_db_connection():
#     app.connection.close()
#     print("Disconnected from the AOT_WIKI database!")

# app.include_router(AOTWikiRouter)