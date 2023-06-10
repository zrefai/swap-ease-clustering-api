import pymongo
from helpers.getEnvVariables import getEnvVariables

envVariables = getEnvVariables()


def get_db():

    client = pymongo.MongoClient(envVariables.MONGO_DB_CONNECTION_STRING)

    return client[envVariables.MONGO_DB_NAME]


if __name__ == '__main__':
    db = get_db()
