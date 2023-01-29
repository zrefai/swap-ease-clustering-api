def aggregateEvents(clustersAndEvents):
    # Aggregate transaction data
    for clusterNumber in clustersAndEvents.keys():
        totalVolume = 0
        highestSale = -1
        lowestSale = float('inf')

        for transaction in clustersAndEvents[clusterNumber]['events']:
            composedPrice = 0 

            if transaction['paymentToken'] == 'ETH' or transaction['paymentToken'] == 'WETH':
                 composedPrice = int(transaction['totalPrice']) / (10 ** 18)

            totalVolume += composedPrice
            highestSale = max(highestSale, composedPrice)
            lowestSale = min(lowestSale, composedPrice)
        
        rankAverage = 0

        for rank in clustersAndEvents[clusterNumber]['nfts'].values():
            rankAverage += rank

        clustersAndEvents[clusterNumber]['totalVolume'] = totalVolume
        clustersAndEvents[clusterNumber]['highestSale'] = highestSale if highestSale != -1 else None
        clustersAndEvents[clusterNumber]['lowestSale'] = lowestSale if lowestSale != float('inf') else None
        clustersAndEvents[clusterNumber]['rankAverage'] = rankAverage / len(clustersAndEvents[clusterNumber]['nfts'].keys())
        clustersAndEvents[clusterNumber]['totalSales'] = len(clustersAndEvents[clusterNumber]['events'])
    
    return list(clustersAndEvents.values())
