# TODO: Can probably move this into generateClustersClass
def addEventsToClusters(events, clusters):
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