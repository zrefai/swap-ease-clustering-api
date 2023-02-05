import unittest
from src.handlers.generateClusters.aggregateEvents import aggregateEvents

class TestAggregateEvents(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.result = aggregateEvents(mockClustersAndEvents)
    
    def test_returns_expected_aggregates_from_valid_events(self):
        self.assertEqual(self.result[0]['totalVolume'], 3.4494199)
        self.assertEqual(self.result[0]['highestSale'], 0.65)
        self.assertEqual(self.result[0]['lowestSale'], 0.3)
        self.assertEqual(self.result[0]['rankAverage'], 7.5)
        self.assertEqual(self.result[0]['totalSales'], 8)
    
    def test_returns_expected_aggregates_from_empty_events(self):
        self.assertEqual(self.result[2]['totalVolume'], 0)
        self.assertEqual(self.result[2]['highestSale'], None)
        self.assertEqual(self.result[2]['lowestSale'], None)
        self.assertEqual(self.result[2]['rankAverage'], 11.5)
        self.assertEqual(self.result[2]['totalSales'], 0)

mockClustersAndEvents = [
  {
    'nfts': { '1': 6, '2': 7, '3': 8, '4': 9 },
    'events': [
      {
        'eventTimestamp': '2022-12-07T21:13:47',
        'paymentToken': 'ETH',
        'tokenId': '1',
        'totalPrice': '397000000000000000'
      },
      {
        'eventTimestamp': '2023-01-06T18:56:35',
        'paymentToken': 'ETH',
        'tokenId': '2',
        'totalPrice': '650000000000000000'
      },
      {
        'eventTimestamp': '2022-11-17T08:09:11',
        'paymentToken': 'WETH',
        'tokenId': '2',
        'totalPrice': '300000000000000000'
      },
      {
        'eventTimestamp': '2022-12-31T08:38:59',
        'paymentToken': 'ETH',
        'tokenId': '3',
        'totalPrice': '649000000000000000'
      },
      {
        'eventTimestamp': '2022-12-30T19:52:11',
        'paymentToken': 'ETH',
        'tokenId': '3',
        'totalPrice': '386899900000000000'
      },
      {
        'eventTimestamp': '2022-12-30T19:45:47',
        'paymentToken': 'WETH',
        'tokenId': '3',
        'totalPrice': '326320000000000000'
      },
      {
        'eventTimestamp': '2022-12-01T07:40:35',
        'paymentToken': 'ETH',
        'tokenId': '4',
        'totalPrice': '379800000000000000'
      },
      {
        'eventTimestamp': '2022-11-30T11:08:59',
        'paymentToken': 'WETH',
        'tokenId': '4',
        'totalPrice': '360400000000000000'
      }
    ]
  },
  {
    'nfts': { '5': 5, '6': 3, '7': 2, '8': 1 },
    'events': [
      {
        'eventTimestamp': '2022-11-22T14:34:23',
        'paymentToken': 'ETH',
        'tokenId': '5',
        'totalPrice': '365000000000000000'
      },
      {
        'eventTimestamp': '2022-11-16T19:35:47',
        'paymentToken': 'ETH',
        'tokenId': '5',
        'totalPrice': '265990000000000000'
      },
      {
        'eventTimestamp': '2022-11-16T00:43:11',
        'paymentToken': 'WETH',
        'tokenId': '5',
        'totalPrice': '220100000000000000'
      },
      {
        'eventTimestamp': '2022-12-05T20:27:11',
        'paymentToken': 'ETH',
        'tokenId': '6',
        'totalPrice': '449000000000000000'
      },
      {
        'eventTimestamp': '2022-12-02T23:25:35',
        'paymentToken': 'ETH',
        'tokenId': '6',
        'totalPrice': '372500000000000000'
      },
      {
        'eventTimestamp': '2022-12-02T21:07:59',
        'paymentToken': 'WETH',
        'tokenId': '6',
        'totalPrice': '332010000000000000'
      }
    ]
  },
  { 'nfts': { '1': 10, '2': 11, '3': 12, '4': 13 }, 'events': [] },
  { 'nfts': { '1': 6, '2': 7, '3': 8, '4': 9 }, 'events': [] }
]


if __name__ == '__main__':
    unittest.main()
