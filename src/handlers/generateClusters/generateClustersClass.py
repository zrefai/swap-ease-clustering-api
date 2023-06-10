import json
import traceback
from apis.alchemy.nftEventsClass import NFTEventsClass
from apis.openSea.eventsClass import EventsClass
from data.clusters import Clusters
from data.collectionNfts.collectionNfts import CollectionNFTs
from data.collectionNfts.collectionNftsDataClasses import CollectionData
from dataProcessing.clusteringAlgorithms.KMeans import getKMeanLabels
from handlers.generateClusters.aggregateEvents import aggregateEvents
from helpers.formatRankedData import formatRankedData


class GenerateClustersClass:
    def __init__(self):
        self.collectionNFTs = CollectionNFTs()
        self.clusters = Clusters()
        self.eventsClass = EventsClass()
        self.nftEventsClass = NFTEventsClass()

    def generateClusters(self, contractAddress: str):
        try:
            # TODO: ensure that contractAddress matches contractAddress stored
            # collectionData = self.collectionNFTs.getCollectionData(
            #     contractAddress)

            # clusters = self.transformDataToClusters(collectionData)
            # print('Getting events')
            events = self.nftEventsClass.getEvents(contractAddress)

            with open("events.txt", "w") as fp:
                json.dump(events, fp)
            # print('Finished retrieving events')
            # eventsAndClusters = self.addEventsToClusters(events, clusters)

            # result = aggregateEvents(eventsAndClusters)

            # result = self.clusters.addClusters(contractAddress, result)

            # if clusters:
            #     return f'Success', 200
            return f'Failure', 500

        except Exception:
            traceback.print_exc()
            print('Could not generate clusters for {}'.format(contractAddress))
            return f'Failure', 500

    # Returns a dictionary of clusters, where each cluster is a dictionary that contains a key - value pair of tokenId - rank
    def transformDataToClusters(self, collectionData: CollectionData):
        # Generate clusters from ranked data
        dataFrame = formatRankedData(collectionData)
        labels = getKMeanLabels(dataFrame)

        print('Finished generating labels')

        clusters = {}

        # Create array for each cluster
        for index, tokenId in enumerate(dataFrame.index):
            # Grab the label from the clusters array
            label = labels[index]

            # Check if label is in dictionary
            if label in clusters.keys():
                # Key - value pair (tokenId - rank)
                clusters[label.item()
                         ][tokenId] = collectionData.collectionData[index].rank
            else:
                clusters[label.item()] = {}
                clusters[label.item()
                         ][tokenId] = collectionData.collectionData[index].rank

        return clusters

    def addEventsToClusters(self, events, clusters):
        eventsAndClusters = {}

        # Add associated events to respective clusters
        for tokenId in events.keys():
            for clusterNumber in clusters.keys():

                # If found, add events and nfts from cluster
                if tokenId in clusters[clusterNumber]:
                    if clusterNumber in eventsAndClusters:
                        eventsAndClusters[clusterNumber]['events'].extend(
                            events[tokenId])
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

        # Sort events within each cluster by eventTimestamp
        for clusterNumber in eventsAndClusters.keys():
            eventsAndClusters[clusterNumber]['events'].sort(
                key=lambda e: e['eventTimestamp'], reverse=True)
            # Restrcuture the data so that timestamp is in ISO format
            eventsAndClusters[clusterNumber]['events'] = [
                {**e, 'eventTimestamp': e['eventTimestamp'].isoformat()} for e in eventsAndClusters[clusterNumber]['events']]

        return list(eventsAndClusters.values())
