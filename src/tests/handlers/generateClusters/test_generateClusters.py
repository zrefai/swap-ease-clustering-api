
import unittest
from unittest.mock import MagicMock, Mock, patch
from src.handlers.generateClusters.generateClustersClass import GenerateClustersClass

class TestGenerateClusters(unittest.TestCase):

    # @patch('src.handlers.generateClusters.generateClustersClass.SortedRankings')
    # @patch('src.handlers.generateClusters.generateClustersClass.Clusters')
    # @patch('src.handlers.generateClusters.generateClustersClass.EventsClass')
    @patch.object(GenerateClustersClass, '__init__', Mock(return_value=None))
    def setUp(self):
        # This SHOULD work but doesnt :(
        # patchSortedRankings().getSortedRankings.return_value = mockSortedRankings
        # patchClusters().addClusters.return_value = True
        # patchEventsClass().getOldEvents.return_value = mockOldEvents

        sortedRankingsMock = MagicMock()
        sortedRankingsMock.getSortedRankings.return_value = mockSortedRankingsData

        clustersMock = MagicMock()
        clustersMock.addClusters.return_value = True

        eventsClassMock = MagicMock()
        eventsClassMock.getOldEvents.return_value = mockOldEventsData

        self.generateClustersClass = GenerateClustersClass()
        self.generateClustersClass.sortedRankings = sortedRankingsMock
        self.generateClustersClass.clusters = clustersMock
        self.generateClustersClass.eventsClass = eventsClassMock
        self.generateClustersClass.transformRankedDataToClusters = MagicMock(return_value=mockTransformRankedDataToClustersData)

        self.contractAddress = 'contractAddress'
    
    def tearDown(self):
        self.generateClustersClass = None
        return super().tearDown()
    
    def test_returnsSuccessResult_whenAllMocksReturnSuccessfully(self):
        result = self.generateClustersClass.generateClusters(self.contractAddress)
        self.assertEqual(result, ('Success', 200))
    
    def test_generatesClusterDataSuccessfullyForCluster1_whenAllMocksReturnSuccessfully(self):
        result = self.generateClustersClass.generateClusters(self.contractAddress)

        generatedClusters = self.generateClustersClass.clusters.addClusters.call_args[0][1]

        expectedNfts = ['5000', '5004']
        expectedEvents = [
            {
                'tokenId': '5000',
                'eventTimestamp': '2023-01-22T23:56:59',
                'totalPrice': '391410000000000000',
                'paymentToken': 'WETH'
            },
            {
                'tokenId': '5004',
                'eventTimestamp': '2023-01-22T23:27:59',
                'totalPrice': '600000000000000000',
                'paymentToken': 'WETH'
            },
            {
                'tokenId': '5004',
                'eventTimestamp': '2023-01-04T20:00:23',
                'totalPrice': '700000000000000000',
                'paymentToken': 'ETH'
            }
        ]

        self.assertEqual(result, ('Success', 200))
        self.assertEqual(len(generatedClusters), 4)

        for index, tokenId in enumerate(generatedClusters[0]['nfts'].keys()):
            self.assertEqual(tokenId, expectedNfts[index])
        
        for index, event in enumerate(generatedClusters[0]['events']):
            self.assertEqual(event, expectedEvents[index])

    def test_generatesClusterDataSuccessfullyForCluster4_whenAllMocksReturnSuccessfully(self):
        result = self.generateClustersClass.generateClusters(self.contractAddress)

        generatedClusters = self.generateClustersClass.clusters.addClusters.call_args[0][1]

        expectedNfts = ['5003', '5008']
        expectedEvents = [
            {
                "tokenId": "5003",
                "eventTimestamp": "2023-01-22T23:27:59",
                "totalPrice": "600000000000000000",
                "paymentToken": "WETH"
            },
            {
                "tokenId": "5003",
                "eventTimestamp": "2023-01-04T20:00:23",
                "totalPrice": "700000000000000000",
                "paymentToken": "ETH"
            }
        ]

        self.assertEqual(result, ('Success', 200))
        self.assertEqual(len(generatedClusters), 4)

        for index, tokenId in enumerate(generatedClusters[3]['nfts'].keys()):
            self.assertEqual(tokenId, expectedNfts[index])
        
        for index, event in enumerate(generatedClusters[3]['events']):
            self.assertEqual(event, expectedEvents[index])

    def test_generatesClusterDataSuccessfully_whenEventsDataIsEmpty(self):
        eventsClassMock = MagicMock()
        eventsClassMock.getOldEvents.return_value = {}

        self.generateClustersClass.eventsClass = eventsClassMock

        result = self.generateClustersClass.generateClusters(self.contractAddress)

        generatedClusters = self.generateClustersClass.clusters.addClusters.call_args[0][1]

        self.assertEqual(result, ('Success', 200))

        for cluster in generatedClusters:
            self.assertEqual(len(cluster['events']), 0)

    def test_returnsFailure_whenAddClustersFailsToAddClusters(self):
        clustersMock = MagicMock()
        clustersMock.addClusters.return_value = None
        
        self.generateClustersClass.clusters = clustersMock

        result = self.generateClustersClass.generateClusters(self.contractAddress)

        self.assertEqual(result, ('Failure', 500))



mockSortedRankingsData = {
    'columns': [
        'Background',
        'Fur',
        'Clothing',
        'Beard',
        'Eye',
        'trait_count'
    ],
    'distributions': [
        {
            'tokenId': '5000',
            'totalScoreDistribution': [
                {
                    'trait_type': 'Background',
                    'score': 5555.0
                },
                {
                    'trait_type': 'Fur',
                    'score': 5555.0
                },
                {
                    'trait_type': 'Clothing',
                    'score': 5555.0
                },
                {
                    'trait_type': 'Eye',
                    'score': 5555.0
                },
                {
                    'trait_type': 'trait_count',
                    'score': 10.0
                },
            ]
        },
        {
            'tokenId': '5001',
            'totalScoreDistribution': [
                {
                    'trait_type': 'Beard',
                    'score': 5555.0
                },
                {
                    'trait_type': 'Fur',
                    'score': 5555.0
                },
                {
                    'trait_type': 'Clothing',
                    'score': 10.0
                },
                {
                    'trait_type': 'Eye',
                    'score': 5555.0
                },
                {
                    'trait_type': 'trait_count',
                    'score': 10.0
                },
            ]
        },
        {
            'tokenId': '5002',
            'totalScoreDistribution': [
                {
                    'trait_type': 'Background',
                    'score': 10.0
                },
                {
                    'trait_type': 'Fur',
                    'score': 5555.0
                },
                {
                    'trait_type': 'Clothing',
                    'score': 20.0
                },
                {
                    'trait_type': 'Eye',
                    'score': 30.0
                },
                {
                    'trait_type': 'trait_count',
                    'score': 10.0
                },
            ]
        },
        {
            'tokenId': '5003',
            'totalScoreDistribution': [
                {
                    'trait_type': 'Beard',
                    'score': 10.0
                },
                {
                    'trait_type': 'Fur',
                    'score': 1.0
                },
                {
                    'trait_type': 'Clothing',
                    'score': 20.0
                },
                {
                    'trait_type': 'Eye',
                    'score': 400.0
                },
                {
                    'trait_type': 'trait_count',
                    'score': 100.0
                },
            ]
        },
    ]
}

mockOldEventsData = {
  '5000': [
    {
      'tokenId': '5000',
      'eventTimestamp': '2023-01-22T23:56:59',
      'totalPrice': '391410000000000000',
      'paymentToken': 'WETH'
    }
  ],
  '5001': [
    {
      'tokenId': '5001',
      'eventTimestamp': '2023-01-22T23:32:35',
      'totalPrice': '502500000000000000',
      'paymentToken': 'ETH'
    }
  ],
  '5002': [
    {
      'tokenId': '5002',
      'eventTimestamp': '2023-01-22T23:27:59',
      'totalPrice': '600000000000000000',
      'paymentToken': 'WETH'
    },
    {
      'tokenId': '5002',
      'eventTimestamp': '2023-01-04T20:00:23',
      'totalPrice': '700000000000000000',
      'paymentToken': 'ETH'
    }
  ],
  '5003': [
    {
      'tokenId': '5003',
      'eventTimestamp': '2023-01-22T23:27:59',
      'totalPrice': '600000000000000000',
      'paymentToken': 'WETH'
    },
    {
      'tokenId': '5003',
      'eventTimestamp': '2023-01-04T20:00:23',
      'totalPrice': '700000000000000000',
      'paymentToken': 'ETH'
    }
  ],
  '5004': [
    {
      'tokenId': '5004',
      'eventTimestamp': '2023-01-22T23:27:59',
      'totalPrice': '600000000000000000',
      'paymentToken': 'WETH'
    },
    {
      'tokenId': '5004',
      'eventTimestamp': '2023-01-04T20:00:23',
      'totalPrice': '700000000000000000',
      'paymentToken': 'ETH'
    }
  ],
  '5005': [
    {
      'tokenId': '5005',
      'eventTimestamp': '2023-01-22T23:27:59',
      'totalPrice': '600000000000000000',
      'paymentToken': 'WETH'
    },
    {
      'tokenId': '5005',
      'eventTimestamp': '2023-01-04T20:00:23',
      'totalPrice': '700000000000000000',
      'paymentToken': 'ETH'
    }
  ]
}

mockTransformRankedDataToClustersData = {
    '0': {
        '5000': 1,
        '5004': 5
    },
    '1': {
        '5001': 2,
        '5005': 6
    },
    '2': {
        '5002': 3,
        '5007': 7
    },
    '3': {
        '5003': 4,
        '5008': 8
    }
}