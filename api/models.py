import uuid
from typing import List
from pydantic import BaseModel, Field
from typing import Optional


class CharacterModel(BaseModel):
    name:str
    about:str
    birth_place:str
    occupation:str
    abilities:list
    race:str

class CharacterUpdateModel(BaseModel):
    id: Optional[str]
    name:str
    about:str
    birth_place:str
    occupation:str
    abilities:list
    race:str

class CharacterModelResponse(BaseModel):
    id: str
    name:str
    about:str
    birth_place:str
    occupation:str
    abilities:list
    race:str


class ResponseBody(BaseModel):
    status:str
    message:Optional[str]
    data:Optional[list]
    error: Optional[str]


class AOTWikiQuery(BaseModel):
    id: str
    name:str
    abilities:list
    race:str
