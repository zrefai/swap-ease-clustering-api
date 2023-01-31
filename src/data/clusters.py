import time
from src.mongoDb import get_db

class Clusters():
    def __init__(self):
        db = get_db()
    
        self.collection = db['clusters']

    def addClusters(self, contractAddress, clustersList):
        currentTime = time.time()

        newDocument = {
            'contractAddress': contractAddress, 
            'createdAt': currentTime, 
            'lastUpdated': currentTime, 
            'clusters': clustersList
        }

        return self.collection.insert_one(newDocument)