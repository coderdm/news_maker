import jsonpickle
import json
import api.db as db


def save(object):
    dbConn = db.getDb()
    try:
        collection = getCollectionName(object)
        data = json.loads(jsonpickle.encode(object, unpicklable=False))
        dbConn[collection].insert_one(data)
    except Exception as ex:
        print('repo - exception' + str(ex))

def findOne(object, key, value):
    dbConn = db.getDb()
    try:
        collection = getCollectionName(object)
        return dbConn[collection].find_one({key: value})
    except Exception as ex:
        print('repo - exception' + str(ex))
    return None

def getCollectionName(object):
    return str(type(object).__name__)