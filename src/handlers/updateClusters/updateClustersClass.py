import datetime
from src.helpers.dateHelpers import getDateBoundary, getDateObject 
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

            # Aggregate new events

            # Update clusters document in DB
            pass
        except:
            print('Could not update clusters for {}'.format(contractAddress))
            # if e.__cause__:
            #     print('Cause:', e.__cause__) 
            
            return f'Failure', 500
    
    def removePastEvents(self, clusters):
        dateBoundary = getDateBoundary(90)

        def filterEvents(event):
            eventTimestampObject = getDateObject(event['eventTimestamp'])

            if eventTimestampObject < dateBoundary:
                return False
            else:
                return True

        for index in range(len(clusters['clusters'])):
            filteredEvents = list(filter(filterEvents, clusters['clusters'][index]['events']))
            clusters['clusters'][index]['events'] = filteredEvents
        
        return clusters
    
    def getLatestEventTimestamp(self, clusters):
        latestEventDate = datetime.datetime(2014, 1, 1)

        for cluster in clusters['clusters']:
            for event in cluster['events']:
                eventTimestampObject = getDateObject(event['eventTimestamp'])

                latestEventDate = max(eventTimestampObject, latestEventDate)
        
        return latestEventDate
    
    def addNewEventsToClusters(self, newEvents, clusters):
        for tokenId in newEvents.keys():
            for cluster in clusters['clusters']:
                # If token is found in a cluster, add their events
                if tokenId in cluster['nfts']:
                    cluster['events'].extend(newEvents[tokenId])
                    break
        
        # TODO: sort by timestamp here
        
        return clusters

