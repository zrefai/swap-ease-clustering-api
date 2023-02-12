def aggregateEvents(clustersAndEvents):
    # Aggregate for whole collection
    collectionTotalVolume = 0
    collectionHighestSale = -1
    collectionLowestSale = float('inf')
    collectionTotalSales = 0

    # Aggregate transaction data
    for cluster in clustersAndEvents:
        totalVolume = 0
        highestSale = -1
        lowestSale = float('inf')

        for transaction in cluster['events']:
            composedPrice = 0 

            if transaction['paymentToken'] == 'ETH' or transaction['paymentToken'] == 'WETH':
                 composedPrice = int(transaction['totalPrice']) / (10 ** 18)

            collectionTotalVolume += composedPrice
            totalVolume += composedPrice

            collectionHighestSale = max(collectionHighestSale, composedPrice)
            highestSale = max(highestSale, composedPrice)

            collectionLowestSale = min(collectionLowestSale, composedPrice)
            lowestSale = min(lowestSale, composedPrice)

            collectionTotalSales += 1
        
        rankAverage = 0

        # TODO: Investigate if this is needed when updating
        for rank in cluster['nfts'].values():
            rankAverage += rank

        cluster['totalVolume'] = totalVolume
        cluster['highestSale'] = highestSale if highestSale != -1 else None
        cluster['lowestSale'] = lowestSale if lowestSale != float('inf') else None
        cluster['rankAverage'] = rankAverage / len(cluster['nfts'].keys())
        cluster['totalSales'] = len(cluster['events'])
    
    return {
        'totalVolume': collectionTotalVolume,
        'highestSale': collectionHighestSale if collectionHighestSale != -1 else None,
        'lowestSale': collectionLowestSale if collectionLowestSale != float('inf') else None,
        'totalSales': collectionTotalSales,
        'clusters': clustersAndEvents
    }
