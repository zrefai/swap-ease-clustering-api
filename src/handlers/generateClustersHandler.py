from data.clusters import Clusters
from dataProcessing.clusteringAlgorithms.KMeans import getKMeanLabels
from helpers.formatRankedData import formatRankedData
from data.sortedRankings import SortedRankings

def generateClustersHandler(contractAddress):
    sortedRanking = SortedRankings()

    # Get distributions data
    rankedData = sortedRanking.getSortedRankings(contractAddress)

    # Generate clusters from ranked data
    dataFrame = formatRankedData(rankedData)
    labels = getKMeanLabels(dataFrame)

    clustersDict = {}

    # Create array for each cluster
    for index, token_id in enumerate(dataFrame.index):
        # Grab the lable from the clusters array
        label = labels[index]
        token_information = {
            "token_id": token_id, 
            "rank": index + 1,
        }

        # Check if label is in dictionary
        if label in clustersDict.keys():
            clustersDict[label.item()].append(token_information)
        else:
            clustersDict[label.item()] = [token_information]


    clusters = Clusters()

    docId = clusters.addCluster(contractAddress, list(clustersDict.values()))

    if docId:
        return f'Success', 200
    else:
        return f'Failure', 500



