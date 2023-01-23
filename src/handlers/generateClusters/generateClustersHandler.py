from src.data.clusters import Clusters
from apis.openSea.getOldEvents import getOldEvents
from src.dataProcessing.clusteringAlgorithms.KMeans import getKMeanLabels
from handlers.generateClusters.addEventsToClusters import addEventsToClusters
from handlers.generateClusters.aggregateEvents import aggregateEvents
from src.helpers.formatRankedData import formatRankedData
from src.data.sortedRankings import SortedRankings

def generateClustersHandler(contractAddress):
    
    # TODO: Check if clusters were already generated
    
    sortedRanking = SortedRankings()

    # Get distributions data
    rankedData = sortedRanking.getSortedRankings(contractAddress)

    # Generate clusters from ranked data
    dataFrame = formatRankedData(rankedData)
    labels = getKMeanLabels(dataFrame)

    clusters = {}

    # Create array for each cluster
    for index, token_id in enumerate(dataFrame.index):
        # Grab the lable from the clusters array
        label = labels[index]
        token_information = {
            "tokenId": token_id, 
            "rank": index + 1,
        }

        # Check if label is in dictionary
        if label in clusters.keys():
            clusters[label.item()].append(token_information)
        else:
            clusters[label.item()] = [token_information]
    
    events = getOldEvents(contractAddress)

    clustersAndEvents = addEventsToClusters(events, clusters)

    result = aggregateEvents(clustersAndEvents)

    # Add document
    clusters = Clusters()
    docId = clusters.addClusters(contractAddress, result)

    if docId:
        return f'Success', 200
    else:
        return f'Failure', 500