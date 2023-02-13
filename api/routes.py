from bson import ObjectId
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from api.models import CharacterModel, ResponseBody, ResponseSuccessMany, ResponseSuccessOne, ResponseError
from api.query import AOTQuery
from api.constants import AOT_WIKI_DB_MODEL_NAME
from fastapi.encoders import jsonable_encoder


AOTWikiRouter = APIRouter(
    prefix='/aot-wiki'
)

@AOTWikiRouter.get('/all')
async def getAllCharacters(request: Request):
    print("Inside getAllCharacters")
    characterModel: CharacterModel = request.app.db[AOT_WIKI_DB_MODEL_NAME]
    characterList = await AOTQuery.getMany(characterModel, {})

    if(len(characterList) == 0):
        return ResponseError(
            status = 404,
            error = "No characters found"
        )
         
    return ResponseSuccessMany(
        status = 200,
        message = "{} characters found".format(len(characterList)),
        data = characterList 
    )


@AOTWikiRouter.get('/{id}')
async def getCharacterById( id: str,request: Request):
    characterModel: CharacterModel = request.app.db[AOT_WIKI_DB_MODEL_NAME]
    character = await AOTQuery.getOne(characterModel, {"_id": ObjectId(id)})

    if(character == None):
        return ResponseError(
            status = 404,
            error = "No character found"
        )
         
        
    return ResponseSuccessOne (
        status = 200,
        message = "character found with id {}".format(id),
        data = character.dict()
    )




@AOTWikiRouter.post('/add')
async def addCharacter(request: Request, character: CharacterModel = Body(...)):
    characterModel: CharacterModel = request.app.db[AOT_WIKI_DB_MODEL_NAME]
    characterToBeAdded  = jsonable_encoder(character)
    addedCharacterResponse = await AOTQuery.addOne(characterModel, characterToBeAdded)
    print(addedCharacterResponse)
    addedCharacterId = str(addedCharacterResponse.inserted_id)

   
    if(addedCharacterId == None):
        return ResponseError (
            status = 500,
            error = "Something went wrong while adding"

        )
    elif(addedCharacterId):
        return ResponseSuccessOne (
            status = 201,
            message = "Character added successfully",
            data = character.dict()
        )

@AOTWikiRouter.put('/update/{id}')
async def updateCharacter(id:str,request: Request, character: CharacterModel = Body(...)):
    characterModel: CharacterModel = request.app.db[AOT_WIKI_DB_MODEL_NAME]
    characterToBeUpdated  = jsonable_encoder(character)

    updatedCharacterResponse = await AOTQuery.updateOne(characterModel, {"_id": ObjectId(id)}, characterToBeUpdated)

    if(updatedCharacterResponse == None):
        return ResponseError (
            status = 404,
            error = "Character with the given id not found"
    )


    return ResponseSuccessOne(
        status = 201,
        message = "Character updated successfully",
        data = character
    )

@AOTWikiRouter.delete('/delete/{id}')
async def deleteCharacter(id:str,request: Request):
    characterModel: CharacterModel = request.app.db[AOT_WIKI_DB_MODEL_NAME]
    deletedCharacterResponse = await AOTQuery.deleteOne(characterModel, {"_id": ObjectId(id)})

    if(deletedCharacterResponse.deleted_count == 0):
        return ResponseError (
            status = 500,
            error = "Something went wrong while deleting"
        )

    elif (deletedCharacterResponse.deleted_count == 1):
        return ResponseSuccessOne (
            status = 200,
            message = "Character deleted successfully",
            data = {}
        )

@AOTWikiRouter.delete('/delete-all')
async def deleteAllCharacters(request: Request):
    characterModel: CharacterModel = request.app.db[AOT_WIKI_DB_MODEL_NAME]
    deletedAllCharacterResponse = await AOTQuery.deleteMany(characterModel, {})

    if(deletedAllCharacterResponse.deleted_count == 0):
        return ResponseError (
            status = 500,
            error = "Something went wrong while deleting"
        )

    elif (deletedAllCharacterResponse.deleted_count > 0):
        return ResponseSuccessMany (
            status = 200,
            message = "{} Characters deleted successfully".format(deletedAllCharacterResponse.deleted_count),
            data = []
        )




   
   
    
   
    

#