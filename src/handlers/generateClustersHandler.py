from data.sortedRankings import SortedRankings
from dataProcessing.clusteringAlgorithms.DBSCAN import getDbscanLabels
from dataProcessing.dimensionReducers.UMAP import createUmapEmbedding
from helpers.formatRankedData import formatRankedData

def generateClustersHandler(contractAddress):
    sortedRankingClass = SortedRankings()

    # Get distributions data
    rankedData = sortedRankingClass.getSortedRankings(contractAddress)

    # Generate clusters from ranked data
    dataFrame = formatRankedData(rankedData)
    umapEmbedding = createUmapEmbedding(dataFrame)
    labels = getDbscanLabels(umapEmbedding)

    clustersDict = {}

    # Create array for each cluster
    for index, token_id in enumerate(dataFrame.index):
        # Grab the lable from the clusters array
        label = labels[index]
        token_information = {
            "token_id": token_id, 
            "rank": index + 1, 
            "token_information": dataFrame.iloc[index].values.tolist()
        }

        # Check if label is in dictionary
        if label in clustersDict.keys():
            clustersDict[label.item()].append(token_information)
        else:
            clustersDict[label.item()] = [token_information]


    return {'data': clustersDict}



