from fastapi import APIRouter, Request
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from pydantic import BaseModel
from api.models import CharacterModel, ResponseBody
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
    characterToBeAdded  = jsonable_encoder(character)
    addedCharacter = await AOTQuery.addOne(characterModel, characterToBeAdded)

    print("addedCharacter: ", addedCharacter)
    if(addedCharacter.inserted_id == None):
        return ResponseBody (
            status = 500,
            error = "Something went wrong while adding"

        )
    elif(len(addedCharacter.inserted_id) > 0):
        return ResponseBody (
            status = 200,
            message = "Character added successfully",
            data = [characterToBeAdded]
        )

   
    

#