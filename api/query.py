from api.models import CharacterModel, AOTWikiQuery
from api.utils import getEntities,getEntity
from pymongo import ReturnDocument

class AOTQuery():
    def __init__(self):
        print("Initialized AOTQuery")

    @staticmethod
    async def getMany(model: CharacterModel, query: AOTWikiQuery):
        return getEntities(model.find(limit=10))

    @staticmethod
    async def getOne(model: CharacterModel, query: AOTWikiQuery):
        return getEntity(model.find_one(query))

    @staticmethod
    async def addOne(model: CharacterModel, character: CharacterModel):
        return model.insert_one(character)

    @staticmethod
    async def updateOne(model: CharacterModel,query: AOTWikiQuery, character: CharacterModel):
        return model.find_one_and_update(query, {"$set": character},  return_document = ReturnDocument.AFTER)

    @staticmethod
    async def deleteOne(model: CharacterModel, query: AOTWikiQuery):
        return model.delete_one(query)

    @staticmethod
    async def deleteMany(model: CharacterModel, query: AOTWikiQuery):
        return model.delete_many(query)