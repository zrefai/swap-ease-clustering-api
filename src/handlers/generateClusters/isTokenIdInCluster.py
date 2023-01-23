def isTokenIdInCluster(cluster, x):
    # Use binary search to search for tokenIds in a cluster
    low = 0
    high = len(cluster) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if int(cluster[mid]["tokenId"]) < x:
            low = mid + 1
        elif int(cluster[mid]["tokenId"]) > x:
            high = mid - 1
        else:
            return True
        
    return False