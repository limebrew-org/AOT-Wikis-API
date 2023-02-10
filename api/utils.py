import json


##! Load Database 
def loadDB():
    with open('db.json','r') as f:
        db = json.load(f)
    f.close()
    return db


##! Save Database 
def saveDB(info:dict):
    with open('db.json','w') as f:
        json.dump(info,f,indent=4)
    f.close()

##! 
def getEntities(dbResponse):
    entityList = []
    for document in dbResponse:
        entityList.append(document)
    return entityList