from bson import ObjectId
from fastapi import APIRouter, Request
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from pydantic import BaseModel
from api.models import CharacterModel, ResponseBody, CharacterUpdateModel
from api.query import AOTQuery
from api.constants import AOT_WIKI_DB_MODEL_NAME
from fastapi.encoders import jsonable_encoder


AOTWikiRouter = APIRouter(
    prefix='/aot-wiki'
)

@AOTWikiRouter.get('/all')
async def getAllCharacters(request: Request):
    characterModel: CharacterModel = request.app.db[AOT_WIKI_DB_MODEL_NAME]
    characterList = await AOTQuery.getMany(characterModel, {})
    print("characterList: ", characterList)

    if(len(characterList) == 0):
        return ResponseBody (
            status = 404,
            error = "No characters were found"
        )
         
        
    return ResponseBody (
        status = 200,
        message = "{} characters found".format(len(characterList)),
        data = characterList 
    )

@AOTWikiRouter.post('/add')
async def addCharacter(request: Request, character: CharacterModel = Body(...)):
    characterModel: CharacterModel = request.app.db[AOT_WIKI_DB_MODEL_NAME]
    print("character: ", character)
    characterToBeAdded  = jsonable_encoder(character)
    print("characterToBeAdded: ", characterToBeAdded)
    addedCharacterResponse = await AOTQuery.addOne(characterModel, characterToBeAdded)
    addedCharacterId = str(addedCharacterResponse.inserted_id)

    print("addedCharacter Id: ", addedCharacterId)
   
    if(addedCharacterId == None):
        return ResponseBody (
            status = 500,
            error = "Something went wrong while adding"

        )
    elif(addedCharacterId):
        return ResponseBody (
            status = 200,
            message = "Character added successfully"
        )

@AOTWikiRouter.put('/update/{id}')
async def updateCharacter(id:str,request: Request, character: CharacterModel = Body(...)):
   characterModel: CharacterModel = request.app.db[AOT_WIKI_DB_MODEL_NAME]
   characterToBeUpdated  = jsonable_encoder(character)
   characterToBeUpdated["_id"] = ObjectId(id)

   ##? Handle bad Request 
   character = {k: v for k, v in character.dict().items() if v is not None}
   print("characterToBeUpdated: ", characterToBeUpdated)

   updatedCharacterResponse = await AOTQuery.updateOne(characterModel, {"_id": ObjectId(id)}, characterToBeUpdated)

   print("updatedCharacter Response: ", updatedCharacterResponse)
   print("updatedCharacter Response Modified Count: ", updatedCharacterResponse.modified_count)
   if(updatedCharacterResponse.modified_count == 0):
        return ResponseBody (
            status = 500,
            error = "Something went wrong while updating"
    )

   elif(updatedCharacterResponse.modified_count > 0):
        return ResponseBody (
            status = 200,
            message = "Character updated successfully"
        )
   
   
    
   
    

#