import datetime
from helpers.dateHelpers import getDateObject
from mongoDb import get_db

class Clusters():
    def __init__(self):
        db = get_db()
    
        self.collection = db['clusters']

    def addClusters(self, contractAddress, clustersObject):
        currentTime = datetime.datetime.utcnow().isoformat()

        newDocument = {
            'contractAddress': contractAddress, 
            'createdAt': currentTime, 
            'lastUpdated': currentTime, 
            **clustersObject
        }

        try:
            result = self.collection.insert_one(newDocument)

            return result.acknowledged

        except:
            print('Could not add clusters to DB for {}'.format(contractAddress))
            raise Exception('Could not add clusters to database for {}'.format(contractAddress))
    
    def getClusters(self, contractAddress):
        try:
            document = self.collection.find_one({'contractAddress': contractAddress})

            if document is None:
                raise TypeError('Clusters document for {} was not found'.format(contractAddress))

            return self.clustersMapper(document)

        except:
            print('Could not retrieve clusters from DB for {}'.format(contractAddress))
            raise Exception('Cannot continue without clusters data')
    
    def updateClusters(self, contractAddress, clustersObject):
        try:
            result = self.collection.update_one({'contractAddress': contractAddress}, {
                '$set': {
                    'lastUpdated': datetime.datetime.utcnow().isoformat(),
                    'totalVolume': clustersObject['totalVolume'],
                    'highestSale': clustersObject['highestSale'],
                    'lowestSale': clustersObject['lowestSale'],
                    'totalSales': clustersObject['totalSales'],
                    'clusters': clustersObject['clusters'],
                }
            })

            return result.acknowledged

        except:
            print('Could not update clusters for {}'.format(contractAddress))
            raise Exception('Could not update clusters for {}'.format(contractAddress))
    
    def clustersMapper(self, document):
        def mapEvent(e):
            return {
                **e,
                'eventTimestamp': getDateObject(e['eventTimestamp']),
            }

        def mapCluster(c):
            return {
                **c,
                'events': list(map(mapEvent, c['events']))
            }
        
        return list(map(mapCluster, document['clusters']))