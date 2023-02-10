import uuid
from typing import List
from pydantic import BaseModel, Field
from typing import Optional


class CharacterModel(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
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
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name:str
    abilities:list
    race:str
