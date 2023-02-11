import json
from api.models import CharacterModelResponse


##?
def getEntities(dbResponse):
    entityList = []
    for document in dbResponse:
        entityModel = CharacterModelResponse(
            id = str(document['_id']),
            name = document['name'],
            about = document['about'],
            birth_place = document['birth_place'],
            occupation = document['occupation'],
            abilities = document['abilities'],
            race = document['race']
        )
        
        entityList.append(entityModel)
    return entityList

##? Handle Environment vaariables
def handleEnv(PYENV):
    if PYENV == 'local':
        return '.env.local'
    if PYENV == 'dev':
        return '.env.dev'
    if PYENV == 'prod':
        return '.env.prod'

