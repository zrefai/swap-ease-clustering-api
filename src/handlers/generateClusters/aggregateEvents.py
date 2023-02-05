# TODO: Change so that it takes a list
def aggregateEvents(clustersAndEvents):
    # Aggregate transaction data

    # TODO: maybe aggregate data as a collection?
    for cluster in clustersAndEvents:
        totalVolume = 0
        highestSale = -1
        lowestSale = float('inf')

        for transaction in cluster['events']:
            composedPrice = 0 

            if transaction['paymentToken'] == 'ETH' or transaction['paymentToken'] == 'WETH':
                 composedPrice = int(transaction['totalPrice']) / (10 ** 18)

            totalVolume += composedPrice
            highestSale = max(highestSale, composedPrice)
            lowestSale = min(lowestSale, composedPrice)
        
        rankAverage = 0

        for rank in cluster['nfts'].values():
            rankAverage += rank

        cluster['totalVolume'] = totalVolume
        cluster['highestSale'] = highestSale if highestSale != -1 else None
        cluster['lowestSale'] = lowestSale if lowestSale != float('inf') else None
        cluster['rankAverage'] = rankAverage / len(cluster['nfts'].keys())
        cluster['totalSales'] = len(cluster['events'])
    
    return clustersAndEvents
