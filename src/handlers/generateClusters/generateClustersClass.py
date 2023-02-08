from src.apis.openSea.eventsClass import EventsClass
from src.data.clusters import Clusters
from src.dataProcessing.clusteringAlgorithms.KMeans import getKMeanLabels
from src.handlers.generateClusters.aggregateEvents import aggregateEvents
from src.helpers.formatRankedData import formatRankedData
from src.data.sortedRankings import SortedRankings

class GenerateClustersClass:
    def __init__(self):
        self.sortedRankings = SortedRankings()
        self.clusters = Clusters()
        self.eventsClass = EventsClass()
    
    def generateClusters(self, contractAddress):
        try:
            rankedData = self.sortedRankings.getSortedRankings(contractAddress)
                
            clusters = self.transformRankedDataToClusters(rankedData)
            events = self.eventsClass.getEvents(contractAddress)
            eventsAndClusters = self.addEventsToClusters(events, clusters)

            result = aggregateEvents(eventsAndClusters)

            result = self.clusters.addClusters(contractAddress, result)

            if result:
                return f'Success', 200
            return f'Failure', 500
            
        except Exception as e:
            print('Could not generate clusters for {}'.format(contractAddress))
            if e.__cause__:
                print(e.__cause__)
            return f'Failure', 500

    def transformRankedDataToClusters(self, rankedData):
        # Generate clusters from ranked data
        dataFrame = formatRankedData(rankedData)
        labels = getKMeanLabels(dataFrame)

        clusters = {}

        # Create array for each cluster
        for index, tokenId in enumerate(dataFrame.index):
            # Grab the lable from the clusters array
            label = labels[index]

            # Check if label is in dictionary
            if label in clusters.keys():
                # Key - value pair (tokenId - rank)
                clusters[label.item()][tokenId] = index + 1
            else:
                clusters[label.item()] = {}
                clusters[label.item()][tokenId] = index + 1
        
        return clusters
    
    def addEventsToClusters(self, events, clusters):
        eventsAndClusters = {}

        # Add associated events to respective clusters
        for tokenId in events.keys():
            for clusterNumber in clusters.keys():

                # If found, add events and nfts from cluster
                if tokenId in clusters[clusterNumber]:
                    if clusterNumber in eventsAndClusters:
                        eventsAndClusters[clusterNumber]['events'].extend(events[tokenId])
                    else:
                        eventsAndClusters[clusterNumber] = {
                            'nfts': clusters[clusterNumber],
                            'events': events[tokenId]
                        }
                    break

        # Add remaining clusters that didnt have events
        for clusterNumber in clusters.keys():
            if clusterNumber not in eventsAndClusters:
                eventsAndClusters[clusterNumber] = {
                            'nfts': clusters[clusterNumber],
                            'events': []
                        }

        for clusterNumber in eventsAndClusters.keys():
            eventsAndClusters[clusterNumber]['events'].sort(key=lambda e: e['eventTimestamp'], reverse=True)
            eventsAndClusters[clusterNumber]['events'] = [{**e, 'eventTimestamp': e['eventTimestamp'].isoformat()} for e in eventsAndClusters[clusterNumber]['events']]
    
        return list(eventsAndClusters.values())