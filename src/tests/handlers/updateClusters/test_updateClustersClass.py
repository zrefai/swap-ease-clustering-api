import datetime
import unittest
from unittest.mock import MagicMock, Mock, patch
from src.handlers.updateClusters.updateClustersClass import UpdateClustersClass
# from freezegun import freeze_time

class TestUpdateClustersClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.patchGetDateBoundary = patch('src.handlers.updateClusters.updateClustersClass.getDateBoundary')
        cls.mockGetDateBoundary = cls.patchGetDateBoundary.start()

        cls.addClassCleanup(cls.patchGetDateBoundary.stop)
    
    @classmethod
    def tearDownClass(cls):
        cls.patchGetDateBoundary.stop()
        return super().tearDownClass()

    @patch.object(UpdateClustersClass, '__init__', Mock(return_value=None))
    def setUp(self):
        clustersMock = MagicMock()
        clustersMock.getClusters.return_value = {}

        self.mockGetDateBoundary.return_value = datetime.datetime.strptime('2023-01-05T12:00:00', '%Y-%m-%dT%H:%M:%S')

        self.updateClustersClass = UpdateClustersClass()
        self.updateClustersClass.clusters = clustersMock
    
    def tearDown(self):
        self.updateClustersClass = None
        return super().tearDown()
    
    def test_removePastEvents_filtersOutPastEventsSuccessfully(self):
        result = self.updateClustersClass.removePastEvents(mockClustersData)

        self.assertEqual(len(result['clusters'][0]['events']), 2)
        self.assertEqual(len(result['clusters'][1]['events']), 2)
        self.assertEqual(len(result['clusters'][2]['events']), 0)
        self.assertEqual(len(result['clusters'][3]['events']), 0)

    def test_removePastEvents_eventsReturnedSuccessfully_whenTimestampsAreGreaterThanDateBoundary(self):
        result = self.updateClustersClass.removePastEvents(mockClustersData)

        self.assertEqual(len(result['clusters'][0]['events']), 2)
        self.assertEqual(len(result['clusters'][1]['events']), 2)

        for event in result['clusters'][0]['events']:
            self.assertGreater(datetime.datetime.strptime(event['eventTimestamp'], '%Y-%m-%dT%H:%M:%S'), self.mockGetDateBoundary.return_value)
        
        for event in result['clusters'][1]['events']:
            self.assertGreater(datetime.datetime.strptime(event['eventTimestamp'], '%Y-%m-%dT%H:%M:%S'), self.mockGetDateBoundary.return_value)
    
    def test_removePastEvents_returnsSuccessfully_whenEventsAreEmpty(self):
        result = self.updateClustersClass.removePastEvents(
            {
                'contractAddress': 'contractAddress',
                'createdAt': 'timestamp-1',
                'lastUpdated': 'timestamp-2',
                'clusters': [{
                    'totalVolume': 0,
                    'highesSale': 0,
                    'lowestSale': 0,
                    'rankAverage': 0,
                    'totalSales': 0,
                    'nfts': { '10': 10, '11': 11, '12': 12, '13': 13 },
                    'events': []
                }]
            })

        self.assertEqual(len(result['clusters'][0]['events']), 0)
    
    def test_getLatestEventTimestamp_returnsLatestEventTimestampSuccessfully(self):
        result = self.updateClustersClass.getLatestEventTimestamp(mockClustersData)

        self.assertEqual(result.isoformat(), '2023-01-07T21:13:47')
    
    def test_getLatestEventTimestamp_returnsDefaultDate_whenClustersHaveNoEvents(self):
        result = self.updateClustersClass.getLatestEventTimestamp(
            {
                'contractAddress': 'contractAddress',
                'createdAt': 'timestamp-1',
                'lastUpdated': 'timestamp-2',
                'clusters': [{
                    'totalVolume': 0,
                    'highesSale': 0,
                    'lowestSale': 0,
                    'rankAverage': 0,
                    'totalSales': 0,
                    'nfts': { '10': 10, '11': 11, '12': 12, '13': 13 },
                    'events': []
                }]
            })
        
        self.assertEqual(result.isoformat(), '2014-01-01T00:00:00')

    
mockClustersData = {
    'contractAddress': 'contractAddress',
    'createdAt': 'timestamp-1',
    'lastUpdated': 'timestamp-2',
    'clusters': [
        {
            'totalVolume': 0,
            'highesSale': 0,
            'lowestSale': 0,
            'rankAverage': 0,
            'totalSales': 0,
            'nfts': { '1': 6, '2': 7, '3': 8, '4': 9 },
            'events': [
                {
                    'eventTimestamp': '2023-01-07T21:13:47',
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
            'totalVolume': 0,
            'highesSale': 0,
            'lowestSale': 0,
            'rankAverage': 0,
            'totalSales': 0,
            'nfts': { '5': 5, '6': 3, '7': 2, '8': 1 },
            'events': [
                {
                    'eventTimestamp': '2023-01-07T20:13:47',
                    'paymentToken': 'ETH',
                    'tokenId': '5',
                    'totalPrice': '397000000000000000'
                },
                {
                    'eventTimestamp': '2023-01-06T18:56:35',
                    'paymentToken': 'ETH',
                    'tokenId': '5',
                    'totalPrice': '650000000000000000'
                },
                {
                    'eventTimestamp': '2022-11-17T08:09:11',
                    'paymentToken': 'WETH',
                    'tokenId': '5',
                    'totalPrice': '300000000000000000'
                },
                {
                    'eventTimestamp': '2022-12-31T08:38:59',
                    'paymentToken': 'ETH',
                    'tokenId': '6',
                    'totalPrice': '649000000000000000'
                },
                {
                    'eventTimestamp': '2022-12-30T19:52:11',
                    'paymentToken': 'ETH',
                    'tokenId': '6',
                    'totalPrice': '386899900000000000'
                },
                {
                    'eventTimestamp': '2022-12-30T19:45:47',
                    'paymentToken': 'WETH',
                    'tokenId': '6',
                    'totalPrice': '326320000000000000'
                },
            ]
        },
        {
            'totalVolume': 0,
            'highesSale': 0,
            'lowestSale': 0,
            'rankAverage': 0,
            'totalSales': 0,
            'nfts': { '10': 10, '11': 11, '12': 12, '13': 13 },
            'events': []
        },
        {
            'totalVolume': 0,
            'highesSale': 0,
            'lowestSale': 0,
            'rankAverage': 0,
            'totalSales': 0,
            'nfts': { '14': 14, '15': 15, '16': 16, '17': 17 },
            'events': []
        }
    ]
}