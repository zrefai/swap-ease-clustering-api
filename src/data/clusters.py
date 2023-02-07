import datetime
import time
from src.helpers.dateHelpers import getDateObject
from src.mongoDb import get_db

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

        # TODO: make it so that it handles from here instead of outside the function
        return self.collection.insert_one(newDocument)
    
    def getClusters(self, contractAddress):
        try:
            document = self.collection.find_one({'contractAddress': contractAddress}, {'clusters': 1})

            if document is None:
                raise TypeError('Clusters document for {} was not found'.format(contractAddress))

            return self.clustersMapper(document)

        except TypeError as e:
            print(e)

            raise Exception('Cannot continue without Clusters data') from e
    
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

            if result.acknowledged == False:
                raise Exception('Could not update document for {}'.format(contractAddress))
        except:
            # TODO: make this more explanatory
            raise Exception()
    
    def clustersMapper(self, document):
        def mapEvent(e):
            return {
                'tokenId': e['asset']['token_id'],
                'eventTimestamp': getDateObject(e['event_timestamp']),
                'totalPrice': e['total_price'],
                'paymentToken': e['payment_token']['symbol'] 
            }

        def mapCluster(c):
            return {
                **c,
                'events': list(map(mapEvent, c['events']))
            }
        
        return list(map(mapCluster, document['clusters']))