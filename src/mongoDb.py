import pymongo
from src.helpers.getEnvVariables import getEnvVariables

envVariables = getEnvVariables()

def get_db():

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = pymongo.MongoClient(envVariables['MONGO_DB_CONNECTION_STRING'])
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client[envVariables['MONGO_DB_NAME']]

if __name__ == '__main__':
    db = get_db()