from src.apis.openSea.eventsClass import EventsClass
from src.data.clusters import Clusters
from src.dataProcessing.clusteringAlgorithms.KMeans import getKMeanLabels
from src.handlers.generateClusters.addEventsToClusters import addEventsToClusters
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
            eventsAndClusters = addEventsToClusters(events, clusters)

            result = aggregateEvents(eventsAndClusters)

            docId = self.clusters.addClusters(contractAddress, result)

            if docId.acknowledged:
                return f'Success', 200
            else:
                return f'Failure', 500
        except:
            print('Could not generate clusters for {}'.format(contractAddress))
            # if e.__cause__:
            #     print('Cause:', e.__cause__)
            
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