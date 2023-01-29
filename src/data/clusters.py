from mongoDb import get_db

class Clusters():
    def __init__(self):
        db = get_db()
    
        self.collection = db['clusters']

    def addClusters(self, contractAddress, clustersList):
        newDocument = {'contractAddress': contractAddress, 'clusters': clustersList}

        return self.collection.insert_one(newDocument)