import time
from src.mongoDb import get_db

class Clusters():
    def __init__(self):
        db = get_db()
    
        self.collection = db['clusters']

    def addClusters(self, contractAddress, clustersObject):
        currentTime = time.time()

        newDocument = {
            'contractAddress': contractAddress, 
            'createdAt': currentTime, 
            'lastUpdated': currentTime, 
            **clustersObject
        }

        return self.collection.insert_one(newDocument)
    
    def getClusters(self, contractAddress):
        try:
            document = self.collection.find_one({'contractAddress': contractAddress})

            if document is None:
                raise TypeError('Clusters document for {} was not found'.format(contractAddress))

            return document
        except TypeError as e:
            print(e)

            raise Exception('Cannot continue without Clusters data') from e