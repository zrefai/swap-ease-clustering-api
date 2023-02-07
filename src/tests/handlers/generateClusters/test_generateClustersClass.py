import unittest
from unittest.mock import MagicMock, Mock, patch
from src.mocks.mockTransformedRankedData import mockTransformedRankedData
from src.mocks.mockProcessedEvents import mockProcessedEvents
from src.handlers.generateClusters.generateClustersClass import GenerateClustersClass

class TestGenerateClustersClass(unittest.TestCase):
    @patch.object(GenerateClustersClass, '__init__', Mock(return_value=None))
    def setUp(self):
        sortedRankingsMock = MagicMock()
        sortedRankingsMock.getSortedRankings.return_value = []

        docIdMock = MagicMock()
        docIdMock.acknowledged = True
        clustersMock = MagicMock()
        clustersMock.addClusters.return_value = docIdMock

        eventsClassMock = MagicMock()
        eventsClassMock.getEvents.return_value = mockProcessedEvents()

        self.generateClustersClass = GenerateClustersClass()
        self.generateClustersClass.sortedRankings = sortedRankingsMock
        self.generateClustersClass.clusters = clustersMock
        self.generateClustersClass.eventsClass = eventsClassMock
        self.generateClustersClass.transformRankedDataToClusters = MagicMock(return_value=mockTransformedRankedData())

        self.contractAddress = 'contractAddress'
    
    def tearDown(self):
        self.generateClustersClass = None
        return super().tearDown()
    
    def test_addEventsToClusters_returnsListWithCorrectNumberOfClusters(self):
        result = self.generateClustersClass.addEventsToClusters(mockProcessedEvents(), mockTransformedRankedData())
        
        self.assertEqual(len(result), 4)

    def test_addEventsToClusters_returnsClusterWithCorrectNfts(self):
        mockClusterValues = list(mockTransformedRankedData()['0'].keys())

        result = self.generateClustersClass.addEventsToClusters(mockProcessedEvents(), mockTransformedRankedData())
        
        # Nfts from cluster 1 appear first in the list because their events are added first
        for index, nft in enumerate(result[0]['nfts']):
            self.assertEqual(nft, mockClusterValues[index])

    def test_addEventsToClusters_returnsCorrectEventsForFirstValue(self):
        mockEventsResult0 = [
            {
                'eventTimestamp': '2022-12-07T21:13:47',
                'paymentToken': 'ETH',
                'tokenId': '5000',
                'totalPrice': '397000000000000000'
            },
            {
                'eventTimestamp': '2022-12-01T07:40:35',
                'paymentToken': 'ETH',
                'tokenId': '5003',
                'totalPrice': '379800000000000000'
            },
            {
                'eventTimestamp': '2022-11-30T11:08:59',
                'paymentToken': 'WETH',
                'tokenId': '5003',
                'totalPrice': '360400000000000000'
            },
            {
                'eventTimestamp': '2022-11-22T14:34:23',
                'paymentToken': 'ETH',
                'tokenId': '5004',
                'totalPrice': '365000000000000000'
            },
            {
                'eventTimestamp': '2022-11-16T19:35:47',
                'paymentToken': 'ETH',
                'tokenId': '5004',
                'totalPrice': '265990000000000000'
            },
            {
                'eventTimestamp': '2022-11-16T00:43:11',
                'paymentToken': 'WETH',
                'tokenId': '5004',
                'totalPrice': '220100000000000000'
            }
        ]

        result = self.generateClustersClass.addEventsToClusters(mockProcessedEvents(), mockTransformedRankedData())

        for index, transaction in enumerate(result[0]['events']):
            self.assertEqual(transaction, mockEventsResult0[index])
    
    def test_addEventsToClusters_returnsCorrectEventsForSecondValue(self):
        mockEventsResult1 = [
            {
                'eventTimestamp': '2023-01-06T18:56:35',
                'paymentToken': 'ETH',
                'tokenId': '5001',
                'totalPrice': '650000000000000000'
            },
            {
                'eventTimestamp': '2022-12-05T20:27:11',
                'paymentToken': 'ETH',
                'tokenId': '5005',
                'totalPrice': '449000000000000000'
            },
            {
                'eventTimestamp': '2022-12-02T23:25:35',
                'paymentToken': 'ETH',
                'tokenId': '5005',
                'totalPrice': '372500000000000000'
            },
            {
                'eventTimestamp': '2022-12-02T21:07:59',
                'paymentToken': 'WETH',
                'tokenId': '5005',
                'totalPrice': '332010000000000000'
            },
            {
                'eventTimestamp': '2022-11-17T08:09:11',
                'paymentToken': 'WETH',
                'tokenId': '5001',
                'totalPrice': '300000000000000000'
            }
        ]

        result = self.generateClustersClass.addEventsToClusters(mockProcessedEvents(), mockTransformedRankedData())

        for index, transaction in enumerate(result[1]['events']):
            self.assertEqual(transaction, mockEventsResult1[index])

    def test_returnsEmptyEventsForClusters_whenTheyHaveNoEvents(self):
        result = self.generateClustersClass.addEventsToClusters(mockProcessedEvents(), mockTransformedRankedData())

        self.assertEqual(len(result[3]['events']), 0)

    def test_returnsSuccessResult_whenAllMocksReturnSuccessfully(self):
        result = self.generateClustersClass.generateClusters(self.contractAddress)

        self.assertEqual(result, ('Success', 200))
    
    def test_generatesClusterDataSuccessfullyForCluster1_whenAllMocksReturnSuccessfully(self):
        result = self.generateClustersClass.generateClusters(self.contractAddress)

        generatedClusters = self.generateClustersClass.clusters.addClusters.call_args[0][1]

        expectedNfts = ['5000', '5003', '5004']
        expectedEvents = [
            {
                'eventTimestamp': '2022-12-07T21:13:47',
                'paymentToken': 'ETH',
                'tokenId': '5000',
                'totalPrice': '397000000000000000'
            },
            {
                'eventTimestamp': '2022-12-01T07:40:35',
                'paymentToken': 'ETH',
                'tokenId': '5003',
                'totalPrice': '379800000000000000'
            },
            {
                'eventTimestamp': '2022-11-30T11:08:59',
                'paymentToken': 'WETH',
                'tokenId': '5003',
                'totalPrice': '360400000000000000'
            },
            {
                'eventTimestamp': '2022-11-22T14:34:23',
                'paymentToken': 'ETH',
                'tokenId': '5004',
                'totalPrice': '365000000000000000'
            },
            {
                'eventTimestamp': '2022-11-16T19:35:47',
                'paymentToken': 'ETH',
                'tokenId': '5004',
                'totalPrice': '265990000000000000'
            },
            {
                'eventTimestamp': '2022-11-16T00:43:11',
                'paymentToken': 'WETH',
                'tokenId': '5004',
                'totalPrice': '220100000000000000'
            }
        ]

        self.assertEqual(result, ('Success', 200))
        self.assertEqual(len(generatedClusters['clusters']), 4)

        for index, tokenId in enumerate(generatedClusters['clusters'][0]['nfts'].keys()):
            self.assertEqual(tokenId, expectedNfts[index])
        
        for index, event in enumerate(generatedClusters['clusters'][0]['events']):
            self.assertEqual(event, expectedEvents[index])
 
    def test_generatesClusterDataSuccessfully_whenEventsDataIsEmpty(self):
        eventsClassMock = MagicMock()
        eventsClassMock.getEvents.return_value = {}

        self.generateClustersClass.eventsClass = eventsClassMock

        result = self.generateClustersClass.generateClusters(self.contractAddress)

        generatedClusters = self.generateClustersClass.clusters.addClusters.call_args[0][1]

        self.assertEqual(result, ('Success', 200))

        for cluster in generatedClusters['clusters']:
            self.assertEqual(len(cluster['events']), 0)

    def test_returnsFailure_whenAddClustersFailsToAddClusters(self):
        docIdMock = MagicMock()
        docIdMock.acknowledged = False
        clustersMock = MagicMock()
        clustersMock.addClusters.return_value = docIdMock
        
        self.generateClustersClass.clusters = clustersMock

        result = self.generateClustersClass.generateClusters(self.contractAddress)

        self.assertEqual(result, ('Failure', 500))
    
    def test_returnsFailure_whenSortedRankingsRaisesRuntimeError(self):
        self.generateClustersClass.sortedRankings.getSortedRankings.side_effect = RuntimeError()

        result = self.generateClustersClass.generateClusters(self.contractAddress)

        self.assertEqual(result, ('Failure', 500))