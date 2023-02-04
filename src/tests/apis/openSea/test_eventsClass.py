from unittest.mock import patch, MagicMock
from src.apis.openSea.eventsClass import EventsClass
import unittest

class TestEventsClass(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.patchTime = patch('time.sleep', return_value=None)
        self.mockTime = self.patchTime.start()

        self.eventsClass = EventsClass()

        mockEnvVariables = MagicMock()
        mockDict = {'OPENSEA_API_KEY': 'apiKey', 'OPENSEA_URL': 'url'}
        mockEnvVariables.__getitem__.side_effect = mockDict.__getitem__

        self.eventsClass.envVariables = mockEnvVariables
        self.contractAddress = 'contractAddress'

        self.addClassCleanup(self.patchTime.stop)

    
    @classmethod
    def tearDownClass(self):
        self.patchTime.stop()

    def setUp(self):
        mockEventsService = MagicMock(side_effect=[mockEvents1, mockEvents2, mockEvents3])
        self.eventsClass.eventsService.getEvents = mockEventsService
    
    def setUp2(self):
        mockEventsService = MagicMock(side_effect=[mockEvents3])
        self.eventsClass.eventsService.getEvents = mockEventsService
    
    def test_returnsCorrectNumberOfKeys_whenEventsAreSuccessful(self):
        self.setUp()
        result = self.eventsClass.getEvents(self.contractAddress)

        self.assertEqual(len(result.keys()), 3)
    
    def test_returnsCorrectNumberOfEvents_whenEventsAreSuccessfullyMerged(self):
        self.setUp()
        result = self.eventsClass.getEvents(self.contractAddress)

        self.assertEqual(len(result['1']), 3)
        self.assertEqual(len(result['2']), 1)
        self.assertEqual(len(result['3']), 1)
    
    def test_returnsCorrectEvents_whenEventsAreSuccessfullyMerged(self):
        self.setUp()
        expectedEvents = [
            {
                'tokenId': '1',
                'eventTimestamp': 'eventTimestamp1',
                'totalPrice': '90',
                'paymentToken': 'ETH'
            },
            {
                'tokenId': '1',
                'eventTimestamp': 'eventTimestamp2',
                'totalPrice': '100',
                'paymentToken': 'ETH'
            },
            {
                'tokenId': '1',
                'eventTimestamp': 'eventTimestamp3',
                'totalPrice': '101',
                'paymentToken': 'ETH'
            },
        ]
        result = self.eventsClass.getEvents(self.contractAddress)

        for index, event in enumerate(result["1"]):
            self.assertEqual(event, expectedEvents[index])
    
    def test_buildsUrlCorrectly_whenCalledWithNoCursor(self):
        expectedResult = 'url/events?asset_contract_address=contractAddress&event_type=successful&occurred_after=unixTime'
        result = self.eventsClass.urlBuilder(self.contractAddress, 'unixTime')

        self.assertEqual(result, expectedResult)
    
    def test_buildsUrlCorrectly_whenCalledWithCursor(self):
        expectedResult = 'url/events?asset_contract_address=contractAddress&event_type=successful&occurred_after=unixTime&cursor=cursor'
        result = self.eventsClass.urlBuilder(self.contractAddress, 'unixTime', 'cursor')

        self.assertEqual(result, expectedResult)
    
    # TODO: add tests for latestTimestamp logic

mockEvents1 = {
    'next': 'cursor1',
    'assetEvents': [
        {
            'tokenId': '1',
            'eventTimestamp': 'eventTimestamp1',
            'totalPrice': '90',
            'paymentToken': 'ETH'
        },
        {
            'tokenId': '2',
            'eventTimestamp': 'eventTimestamp2',
            'totalPrice': '90',
            'paymentToken': 'ETH'
        },
        {
            'tokenId': '3',
            'eventTimestamp': 'eventTimestamp1',
            'totalPrice': '90',
            'paymentToken': 'ETH'
        }
    ]
}

mockEvents2 = {
    'next': 'cursor2',
    'assetEvents': [
        {
            'tokenId': '1',
            'eventTimestamp': 'eventTimestamp2',
            'totalPrice': '100',
            'paymentToken': 'ETH'
        }
    ]
}

mockEvents3 = {
    'next': None,
    'assetEvents': [
        {
            'tokenId': '1',
            'eventTimestamp': 'eventTimestamp3',
            'totalPrice': '101',
            'paymentToken': 'ETH'
        }
    ]
}