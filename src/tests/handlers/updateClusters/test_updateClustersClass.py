import datetime
import unittest
from unittest.mock import MagicMock, Mock, patch
from mocks.mockProcessedEvents import mockProcessedEvents
from mocks.mockProcessedClusters import mockProcessedClusters
from helpers.dateHelpers import getDateObject
from handlers.updateClusters.updateClustersClass import UpdateClustersClass

class TestUpdateClustersClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.patchGetDateBoundary = patch('handlers.updateClusters.updateClustersClass.getDateBoundary')
        cls.mockGetDateBoundary = cls.patchGetDateBoundary.start()

        cls.addClassCleanup(cls.patchGetDateBoundary.stop)
    
    @classmethod
    def tearDownClass(cls):
        cls.patchGetDateBoundary.stop()
        return super().tearDownClass()

    @patch.object(UpdateClustersClass, '__init__', Mock(return_value=None))
    def setUp(self):
        clustersMock = MagicMock()
        clustersMock.getClusters.return_value = mockProcessedClusters()
        clustersMock.updateClusters.return_value = True

        eventsClassMock = MagicMock()
        eventsClassMock.getEvents.return_value = mockProcessedEvents()

        self.mockGetDateBoundary.return_value = datetime.datetime.strptime('2023-01-05T12:00:00', '%Y-%m-%dT%H:%M:%S')

        self.updateClustersClass = UpdateClustersClass()
        self.updateClustersClass.clusters = clustersMock
        self.updateClustersClass.eventsClass = eventsClassMock
    
    def tearDown(self):
        self.updateClustersClass = None
        return super().tearDown()
    
    def test_removePastEvents_filtersOutPastEventsSuccessfully(self):
        result = self.updateClustersClass.removePastEvents(mockProcessedClusters())

        self.assertEqual(len(result[0]['events']), 2)
        self.assertEqual(len(result[1]['events']), 2)
        self.assertEqual(len(result[2]['events']), 0)
        self.assertEqual(len(result[3]['events']), 0)

    def test_removePastEvents_eventsReturnedSuccessfully_whenTimestampsAreGreaterThanDateBoundary(self):
        result = self.updateClustersClass.removePastEvents(mockProcessedClusters())

        self.assertEqual(len(result[0]['events']), 2)
        self.assertEqual(len(result[1]['events']), 2)

        for event in result[0]['events']:
            self.assertGreater(event['eventTimestamp'], self.mockGetDateBoundary.return_value)
        
        for event in result[1]['events']:
            self.assertGreater(event['eventTimestamp'], self.mockGetDateBoundary.return_value)
    
    def test_removePastEvents_returnsSuccessfully_whenEventsAreEmpty(self):
        result = self.updateClustersClass.removePastEvents(
            [{
                'totalVolume': 0,
                'highestSale': 0,
                'lowestSale': 0,
                'rankAverage': 0,
                'totalSales': 0,
                'nfts': { '10': 10, '11': 11, '12': 12, '13': 13 },
                'events': []
            }])

        self.assertEqual(len(result[0]['events']), 0)
    
    def test_getLatestEventTimestamp_returnsLatestEventTimestampSuccessfully(self):
        result = self.updateClustersClass.getLatestEventTimestamp(mockProcessedClusters())

        self.assertEqual(result, getDateObject('2023-01-07T21:13:47'))
    
    def test_getLatestEventTimestamp_returnsDefaultDate_whenClustersHaveNoEvents(self):
        result = self.updateClustersClass.getLatestEventTimestamp(
            [{
                'totalVolume': 0,
                'highestSale': 0,
                'lowestSale': 0,
                'rankAverage': 0,
                'totalSales': 0,
                'nfts': { '10': 10, '11': 11, '12': 12, '13': 13 },
                'events': []
            }])
        
        self.assertEqual(result.isoformat(), '2014-01-01T00:00:00')
    
    def test_addNewEventsToClusters_returnsCorrectEventsForFirstCluster(self):
        mockEventsResult0 = [
            {
                'eventTimestamp': '2023-01-07T21:13:47',
                'paymentToken': 'ETH',
                'tokenId': '5001',
                'totalPrice': '397000000000000000'
            },
            {
                'eventTimestamp': '2023-01-06T18:56:35',
                'paymentToken': 'ETH',
                'tokenId': '5000',
                'totalPrice': '650000000000000000'
            },
            {
                'eventTimestamp': '2022-12-31T08:38:59',
                'paymentToken': 'ETH',
                'tokenId': '5003',
                'totalPrice': '649000000000000000'
            },
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
                'eventTimestamp': '2022-11-17T08:09:11',
                'paymentToken': 'WETH',
                'tokenId': '5000',
                'totalPrice': '300000000000000000'
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

        result = self.updateClustersClass.addNewEventsToClusters(mockProcessedEvents(), mockProcessedClusters())

        for index, transaction in enumerate(result[0]['events']):
            self.assertEqual(transaction, mockEventsResult0[index])
    
    def test_addNewEventsToClusters_returnsCorrectEventsForSecondCluster(self):
        mockEventsResult1 = [
            {
                'eventTimestamp': '2023-01-07T20:13:47',
                'paymentToken': 'ETH',
                'tokenId': '5005',
                'totalPrice': '397000000000000000'
            },
            {
                'eventTimestamp': '2023-01-06T18:56:35',
                'paymentToken': 'ETH',
                'tokenId': '5005',
                'totalPrice': '650000000000000000'
            },
            {
                'eventTimestamp': '2023-01-06T18:56:35',
                'paymentToken': 'ETH',
                'tokenId': '5001',
                'totalPrice': '650000000000000000'
            },
            {
                'eventTimestamp': '2022-12-31T08:38:59',
                'paymentToken': 'ETH',
                'tokenId': '5006',
                'totalPrice': '649000000000000000'
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
                'tokenId': '5005',
                'totalPrice': '300000000000000000'
            },
            {
                'eventTimestamp': '2022-11-17T08:09:11',
                'paymentToken': 'WETH',
                'tokenId': '5001',
                'totalPrice': '300000000000000000'
            }
        ]

        result = self.updateClustersClass.addNewEventsToClusters(mockProcessedEvents(), mockProcessedClusters())

        for index, transaction in enumerate(result[1]['events']):
            self.assertEqual(transaction, mockEventsResult1[index])

    def test_updateClusters_returnsSuccess_whenClustersAreUpdated(self):
        result = self.updateClustersClass.updateClusters('contractAddress')

        self.assertEqual(result, ('Success', 200))
    
    def test_updateClusters_returnsFailure_whenUpdatingClustersThrowsException(self):
        clustersMock = MagicMock()
        clustersMock.getClusters.return_value = mockProcessedClusters()
        clustersMock.updateClusters.side_effect = Exception('Could not update clusters in DB')

        self.updateClustersClass.clusters = clustersMock

        result = self.updateClustersClass.updateClusters('contractAddress')

        self.assertEqual(result, ('Failure', 500))
    
    def test_updateClusters_returnsFailure_whenGetEventsThrowsException(self):
        eventsClassMock = MagicMock()
        eventsClassMock.getEvents.side_effect = Exception('Could not get events')

        self.updateClustersClass.eventsClass = eventsClassMock

        result = self.updateClustersClass.updateClusters('contractAddress')

        self.assertEqual(result, ('Failure', 500))

    def test_updateClusters_firstClusterPassedToUpdateClustersIsCorrect(self):
        result = self.updateClustersClass.updateClusters('contractAddress')

        updatedClusters = self.updateClustersClass.clusters.updateClusters.call_args[0][1]

        mockAggregates = {
            'totalVolume': 3.03529,
            'highestSale': 0.65,
            'lowestSale': 0.2201,
            'rankAverage': 30.75,
            'totalSales': 8,
        }
        mockEvents = [
            {
                'eventTimestamp': '2023-01-07T21:13:47',
                'paymentToken': 'ETH',
                'tokenId': '5001',
                'totalPrice': '397000000000000000'
            },
            {
                'eventTimestamp': '2023-01-06T18:56:35',
                'paymentToken': 'ETH',
                'tokenId': '5000',
                'totalPrice': '650000000000000000'
            },
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

        for index, transaction in enumerate(updatedClusters['clusters'][0]['events']):
            self.assertEqual(transaction, mockEvents[index])
        
        for key in mockAggregates.keys():
            self.assertEqual(mockAggregates[key], updatedClusters['clusters'][0][key])

    def test_updateClusters_collectionAggregatesPassedToUpdateClustersIsCorrect(self):
        result = self.updateClustersClass.updateClusters('contractAddress')

        updatedClusters = self.updateClustersClass.clusters.updateClusters.call_args[0][1]

        mockAggregates = {
            'totalVolume': 6.1858,
            'highestSale': 0.65,
            'lowestSale': 0.2201,
            'totalSales': 15,
        }

        self.assertEqual(result, ('Success', 200))
        
        for key in mockAggregates.keys():
            self.assertEqual(mockAggregates[key], updatedClusters[key])

