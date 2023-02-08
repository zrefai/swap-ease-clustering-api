import datetime
from src.handlers.generateClusters.aggregateEvents import aggregateEvents
from src.helpers.dateHelpers import getDateBoundary 
from src.apis.openSea.eventsClass import EventsClass
from src.data.clusters import Clusters

class UpdateClustersClass:
    def __init__(self):
        self.clusters = Clusters()
        self.eventsClass = EventsClass()
    
    def updateClusters(self, contractAddress):
        try:
            clusters = self.clusters.getClusters(contractAddress)
            
            self.removePastEvents(clusters)
            newEvents = self.eventsClass.getEvents(contractAddress, self.getLatestEventTimestamp(clusters))
            self.addNewEventsToClusters(newEvents, clusters)

            result = aggregateEvents(clusters)

            result = self.clusters.updateClusters(contractAddress, result)

            if result:
                return f'Success', 200
            return f'Failure', 500
            
        except Exception as e:
            print('Could not update clusters for {}'.format(contractAddress))
            if e.__cause__:
                print(e.__cause__)
            return f'Failure', 500
    
    def removePastEvents(self, clusters):
        dateBoundary = getDateBoundary(90)

        def filterEvents(event):
            eventTimestampObject = event['eventTimestamp']

            if eventTimestampObject < dateBoundary:
                return False
            else:
                return True

        for index in range(len(clusters)):
            filteredEvents = list(filter(filterEvents, clusters[index]['events']))
            clusters[index]['events'] = filteredEvents
        
        return clusters
    
    def getLatestEventTimestamp(self, clusters):
        latestEventDate = datetime.datetime(2014, 1, 1)

        for cluster in clusters:
            for event in cluster['events']:
                latestEventDate = max(event['eventTimestamp'], latestEventDate)
        
        return latestEventDate
    
    def addNewEventsToClusters(self, newEvents, clusters):
        for tokenId in newEvents.keys():
            for cluster in clusters:
                # If token is found in a cluster, add their events
                if tokenId in cluster['nfts']:
                    cluster['events'].extend(newEvents[tokenId])
                    break
        
        for cluster in clusters:
            cluster['events'].sort(key=lambda e: e['eventTimestamp'], reverse=True)
            cluster['events'] = [{**e, 'eventTimestamp': e['eventTimestamp'].isoformat()} for e in cluster['events']]
        
        return clusters

