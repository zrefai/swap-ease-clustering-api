import unittest
from src.handlers.generateClusters.addEventsToClusters import addEventsToClusters

class TestAddEventsToClusters(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.clustersAndEvents = addEventsToClusters(mockEvents, mockClusters)
    
    def test_returns_object_with_correct_amount_of_clusters(self):
        self.assertEqual(len(self.clustersAndEvents.keys()), 4)

    def test_returns_cluster_with_all_nfts_from_clusters(self):
        mockClusterValues = list(mockClusters["0"].keys())
        for index, nft in enumerate(self.clustersAndEvents["0"]["nfts"]):
            self.assertEqual(nft, mockClusterValues[index])

    def test_returns_cluster_0_with_correct_events(self):
        mockEventsResult0 = [
            {
                "eventTimestamp": "2022-11-22T14:34:23",
                "paymentToken": "ETH",
                "tokenId": "5",
                "totalPrice": "365000000000000000"
            },
            {
                "eventTimestamp": "2022-11-16T19:35:47",
                "paymentToken": "ETH",
                "tokenId": "5",
                "totalPrice": "265990000000000000"
            },
            {
                "eventTimestamp": "2022-11-16T00:43:11",
                "paymentToken": "WETH",
                "tokenId": "5",
                "totalPrice": "220100000000000000"
            },
            {
                "eventTimestamp": "2022-12-05T20:27:11",
                "paymentToken": "ETH",
                "tokenId": "6",
                "totalPrice": "449000000000000000"
            },
            {
                "eventTimestamp": "2022-12-02T23:25:35",
                "paymentToken": "ETH",
                "tokenId": "6",
                "totalPrice": "372500000000000000"
            },
            {
                "eventTimestamp": "2022-12-02T21:07:59",
                "paymentToken": "WETH",
                "tokenId": "6",
                "totalPrice": "332010000000000000"
            }
        ]

        for index, transaction in enumerate(self.clustersAndEvents["0"]["events"]):
            self.assertEqual(transaction, mockEventsResult0[index])
    
    def test_returns_cluster_1_with_correct_events(self):
        mockEventsResult1 = [
            {
                "eventTimestamp": "2022-12-07T21:13:47",
                "paymentToken": "ETH",
                "tokenId": "1",
                "totalPrice": "397000000000000000"
            },
            {
                "eventTimestamp": "2023-01-06T18:56:35",
                "paymentToken": "ETH",
                "tokenId": "2",
                "totalPrice": "650000000000000000"
            },
            {
                "eventTimestamp": "2022-11-17T08:09:11",
                "paymentToken": "WETH",
                "tokenId": "2",
                "totalPrice": "300000000000000000"
            },
            {
                "eventTimestamp": "2022-12-31T08:38:59",
                "paymentToken": "ETH",
                "tokenId": "3",
                "totalPrice": "649000000000000000"
            },
            {
                "eventTimestamp": "2022-12-30T19:52:11",
                "paymentToken": "ETH",
                "tokenId": "3",
                "totalPrice": "386899900000000000"
            },
            {
                "eventTimestamp": "2022-12-30T19:45:47",
                "paymentToken": "WETH",
                "tokenId": "3",
                "totalPrice": "326320000000000000"
            },
            {
                "eventTimestamp": "2022-12-01T07:40:35",
                "paymentToken": "ETH",
                "tokenId": "4",
                "totalPrice": "379800000000000000"
            },
            {
                "eventTimestamp": "2022-11-30T11:08:59",
                "paymentToken": "WETH",
                "tokenId": "4",
                "totalPrice": "360400000000000000"
            },
        ]

        for index, transaction in enumerate(self.clustersAndEvents["1"]["events"]):
            self.assertEqual(transaction, mockEventsResult1[index])

    def test_returns_empty_events_for_other_clusters(self):
        self.assertEqual(len(self.clustersAndEvents["2"]["events"]), 0)
        self.assertEqual(len(self.clustersAndEvents["3"]["events"]), 0)


mockClusters = {
    "0": {
        "5": 5,
        "6": 3,
        "7": 2,
        "8": 1
    },
    "1": {
        "1": 6,
        "2": 7,
        "3": 8,
        "4": 9
    },
    "2": {
        "1": 6,
        "2": 7,
        "3": 8,
        "4": 9
    },
    "3": {
        "1": 6,
        "2": 7,
        "3": 8,
        "4": 9
    }
}

mockEvents = {
    "1": [
        {
            "eventTimestamp": "2022-12-07T21:13:47",
            "paymentToken": "ETH",
            "tokenId": "1",
            "totalPrice": "397000000000000000"
        }
    ],
    "2": [
        {
            "eventTimestamp": "2023-01-06T18:56:35",
            "paymentToken": "ETH",
            "tokenId": "2",
            "totalPrice": "650000000000000000"
        },
        {
            "eventTimestamp": "2022-11-17T08:09:11",
            "paymentToken": "WETH",
            "tokenId": "2",
            "totalPrice": "300000000000000000"
        }
    ],
    "3": [
        {
            "eventTimestamp": "2022-12-31T08:38:59",
            "paymentToken": "ETH",
            "tokenId": "3",
            "totalPrice": "649000000000000000"
        },
        {
            "eventTimestamp": "2022-12-30T19:52:11",
            "paymentToken": "ETH",
            "tokenId": "3",
            "totalPrice": "386899900000000000"
        },
        {
            "eventTimestamp": "2022-12-30T19:45:47",
            "paymentToken": "WETH",
            "tokenId": "3",
            "totalPrice": "326320000000000000"
        }
    ],
    "4": [
        {
            "eventTimestamp": "2022-12-01T07:40:35",
            "paymentToken": "ETH",
            "tokenId": "4",
            "totalPrice": "379800000000000000"
        },
        {
            "eventTimestamp": "2022-11-30T11:08:59",
            "paymentToken": "WETH",
            "tokenId": "4",
            "totalPrice": "360400000000000000"
        }
    ],
    "5": [
        {
            "eventTimestamp": "2022-11-22T14:34:23",
            "paymentToken": "ETH",
            "tokenId": "5",
            "totalPrice": "365000000000000000"
        },
        {
            "eventTimestamp": "2022-11-16T19:35:47",
            "paymentToken": "ETH",
            "tokenId": "5",
            "totalPrice": "265990000000000000"
        },
        {
            "eventTimestamp": "2022-11-16T00:43:11",
            "paymentToken": "WETH",
            "tokenId": "5",
            "totalPrice": "220100000000000000"
        }
    ],
    "6": [
        {
            "eventTimestamp": "2022-12-05T20:27:11",
            "paymentToken": "ETH",
            "tokenId": "6",
            "totalPrice": "449000000000000000"
        },
        {
            "eventTimestamp": "2022-12-02T23:25:35",
            "paymentToken": "ETH",
            "tokenId": "6",
            "totalPrice": "372500000000000000"
        },
        {
            "eventTimestamp": "2022-12-02T21:07:59",
            "paymentToken": "WETH",
            "tokenId": "6",
            "totalPrice": "332010000000000000"
        }
    ],
}

if __name__ == '__main__':
    unittest.main()