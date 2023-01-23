import unittest
from src.handlers.generateClusters.isTokenIdInCluster import isTokenIdInCluster

class TestIsTokenIdInCluster(unittest.TestCase):
    def test_returns_false_with_empty_cluster(self):
        data = []
        result = isTokenIdInCluster(data, 1001)
        self.assertEqual(result, False)

    def test_returns_true_with_valid_cluster(self):
        data = [
            {
                "tokenId": "20",
                "rank": 1
            },
            {
                "tokenId": "22",
                "rank": 2
            },
            {
                "tokenId": "50",
                "rank": 3
            },
            {
                "tokenId": "100",
                "rank": 4
            },
            {
                "tokenId": "1000",
                "rank": 5
            },
            {
                "tokenId": "1001",
                "rank": 6
            },
            {
                "tokenId": "5000",
                "rank": 7
            },
        ]

        result = isTokenIdInCluster(data, 1001)
        self.assertEqual(result, True)

    def test_returns_false_with_valid_cluster(self):
        data = [
            {
                "tokenId": "20",
                "rank": 1
            },
            {
                "tokenId": "22",
                "rank": 2
            },
            {
                "tokenId": "50",
                "rank": 3
            },
            {
                "tokenId": "100",
                "rank": 4
            },
            {
                "tokenId": "1000",
                "rank": 5
            },
            {
                "tokenId": "1001",
                "rank": 6
            },
            {
                "tokenId": "5000",
                "rank": 7
            },
        ]

        result = isTokenIdInCluster(data, 55)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()