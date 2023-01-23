from src.handlers.generateClusters.isTokenIdInCluster import isTokenIdInCluster

def addEventsToClusters(events, clusters):
    clustersAndEvents = {}

    # Add associated events to respective clusters
    for tokenId in events.keys():
        for clusterNumber in clusters.keys():
            # Search for tokenId in cluster
            result = isTokenIdInCluster(clusters[clusterNumber], int(tokenId))

            # If found, add events and nfts from cluster
            if result:
                if clusterNumber in clustersAndEvents:
                    clustersAndEvents[clusterNumber]["events"].extend(events[tokenId])
                else:
                    clustersAndEvents[clusterNumber] = {
                        "nfts": clusters[clusterNumber],
                        "events": events[tokenId]
                    }
                break

    # Add remaining clusters that didnt have events
    for clusterNumber in clusters.keys():
        if clusterNumber not in clustersAndEvents:
            clustersAndEvents[clusterNumber] = {
                        "nfts": clusters[clusterNumber],
                        "events": []
                    }

    return clustersAndEvents