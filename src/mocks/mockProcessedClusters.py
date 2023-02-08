from src.helpers.dateHelpers import getDateObject

def mockProcessedClusters():
    return [
        {
            'totalVolume': 0,
            'highestSale': 0,
            'lowestSale': 0,
            'rankAverage': 0,
            'totalSales': 0,
            'nfts': { '5000': 6, '50002': 8, '5003': 9, '5004': 100 },
            'events': [
                {
                    'eventTimestamp': getDateObject('2023-01-07T21:13:47'),
                    'paymentToken': 'ETH',
                    'tokenId': '5001',
                    'totalPrice': '397000000000000000'
                },
                {
                    'eventTimestamp': getDateObject('2023-01-06T18:56:35'),
                    'paymentToken': 'ETH',
                    'tokenId': '5000',
                    'totalPrice': '650000000000000000'
                },
                {
                    'eventTimestamp': getDateObject('2022-11-17T08:09:11'),
                    'paymentToken': 'WETH',
                    'tokenId': '5000',
                    'totalPrice': '300000000000000000'
                },
                {
                    'eventTimestamp': getDateObject('2022-12-31T08:38:59'),
                    'paymentToken': 'ETH',
                    'tokenId': '5003',
                    'totalPrice': '649000000000000000'
                },
            ]
        },
        {
            'totalVolume': 0,
            'highestSale': 0,
            'lowestSale': 0,
            'rankAverage': 0,
            'totalSales': 0,
            'nfts': { '5001': 5, '5005': 3, '5006': 2, '5007': 1 },
            'events': [
                {
                    'eventTimestamp': getDateObject('2023-01-07T20:13:47'),
                    'paymentToken': 'ETH',
                    'tokenId': '5005',
                    'totalPrice': '397000000000000000'
                },
                {
                    'eventTimestamp': getDateObject('2023-01-06T18:56:35'),
                    'paymentToken': 'ETH',
                    'tokenId': '5005',
                    'totalPrice': '650000000000000000'
                },
                {
                    'eventTimestamp': getDateObject('2022-11-17T08:09:11'),
                    'paymentToken': 'WETH',
                    'tokenId': '5005',
                    'totalPrice': '300000000000000000'
                },
                {
                    'eventTimestamp': getDateObject('2022-12-31T08:38:59'),
                    'paymentToken': 'ETH',
                    'tokenId': '5006',
                    'totalPrice': '649000000000000000'
                },
            ]
        },
        {
            'totalVolume': 0,
            'highestSale': 0,
            'lowestSale': 0,
            'rankAverage': 0,
            'totalSales': 0,
            'nfts': { '5010': 10, '5011': 11, '5012': 12, '5013': 13 },
            'events': []
        },
        {
            'totalVolume': 0,
            'highestSale': 0,
            'lowestSale': 0,
            'rankAverage': 0,
            'totalSales': 0,
            'nfts': { '5014': 14, '5015': 15, '5016': 16, '5017': 17 },
            'events': []
        }
    ]