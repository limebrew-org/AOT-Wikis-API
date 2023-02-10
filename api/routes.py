from fastapi import APIRouter, Request
from pydantic import BaseModel
from db import AOT_WIKI_DB

class ResponseBody(BaseModel):
    status:str
    message:str
    data:list

class Info(BaseModel):
    name:str
    about:str
    birth_place:str
    occupation:str
    abilities:str
    race:str


AOTWikiRouter = APIRouter(
    prefix='/aot-wiki'
)


@AOTWikiRouter.get('/all')
def getAllCharacters():
    return ResponseBody(
        status=200, 
        message='{} Characters were found'.format(len(AOT_WIKI_DB)),
        data= AOT_WIKI_DB
    )

##TODO: Get a specific character
@AOTWikiRouter.get('/')
def getCharacterByQuery(name:str='',birth_place:str='',race:str=''):
    if(len(name) > 0):
        filteredCharacters = list(filter(lambda character: name in character['name'], AOT_WIKI_DB))
    elif(len(birth_place)>0):
        filteredCharacters = list(filter(lambda character: birth_place in character['birth_place'], AOT_WIKI_DB))
    elif(len(race)>0):
        filteredCharacters = list(filter(lambda character: race in character['race'], AOT_WIKI_DB))
    

    return ResponseBody(
        status= 200,
        message="{} Characters were filtered".format(len(filteredCharacters)),
        data = filteredCharacters
    )

##TODO: Add a new character
@AOTWikiRouter.post('/add')
async def addNewCharacter(character_info:Info):
    ##? Add the character to the database/list
    AOT_WIKI_DB.append(character_info.dict())

    return ResponseBody(
        status = 200,
        message = "Character added successfully",
        data = []
    )    
