from fastapi import APIRouter
from pydantic import BaseModel
from db import AOT_WIKI_DB

class ResponseBody(BaseModel):
    status:str
    message:str
    data:list

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


@AOTWikiRouter.get('/')
def getCharacterByQuery(name:str='',birth_place:str='',race:str=''):
    if(len(name) > 0):
        filteredCharacters = list(filter(lambda character: name in character['name'], AOT_WIKI_DB))
    elif(len(birth_place)>0):
        filteredCharacters = list(filter(lambda character: birth_place in character['birth_place'], AOT_WIKI_DB))
    elif(len(race)>0):
        filteredCharacters = list(filter(lambda character: race in character['race'], AOT_WIKI_DB))
    
    print(filteredCharacters)
    return ResponseBody(
        status= 200,
        message="{} Characters were filtered".format(len(filteredCharacters)),
        data = filteredCharacters
    )