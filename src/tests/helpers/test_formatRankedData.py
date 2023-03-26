import unittest
import pandas as pd
from helpers.formatRankedData import formatRankedData

class TestFormatRankedData(unittest.TestCase):

    def test_formatRankedData_emptyInput(self):
        input_data = {"columns": [], "distributions": []}
        
        expected_output = pd.DataFrame()
        expected_output.index.name = 'tokenId'

        result = formatRankedData(input_data)

        pd.testing.assert_frame_equal(result, expected_output)

    def test_formatRankedData_singleEntry(self):
        input_data = {
            "columns": ["Hat"],
            "distributions": [
                {
                    "tokenId": "1",
                    "totalScoreDistribution": [
                        {
                            "traitType": "Hat",
                            "score": 153.84615384615384
                        }
                    ]
                }
            ]
        }
        expected_output = pd.DataFrame(columns=['Hat'], index=['1'])
        expected_output.index.name = 'tokenId'
        expected_output.iloc[0] = [153.84615384615384]

        result = formatRankedData(input_data)

        pd.testing.assert_frame_equal(result, expected_output)

    def test_formatRankedData_multipleEntries(self):
        input_data = {
            "columns": ["Hat", "Mouth"],
            "distributions": [
                {
                    "tokenId": "1",
                    "totalScoreDistribution": [
                        {
                            "traitType": "Hat",
                            "score": 153.84615384615384
                        },
                        {
                            "traitType": "Mouth",
                            "score": 120.5
                        }
                    ]
                },
                {
                    "tokenId": "2",
                    "totalScoreDistribution": [
                        {
                            "traitType": "Hat",
                            "score": 95.123
                        },
                        {
                            "traitType": "Mouth",
                            "score": 80.0
                        }
                    ]
                }
            ]
        }
        expected_output = pd.DataFrame(columns=['Hat', 'Mouth'], index=['1', '2'])
        expected_output.index.name = 'tokenId'
        expected_output.iloc[0] = [153.84615384615384,  120.5]
        expected_output.iloc[1] = [95.123,  80.0]
    
        result = formatRankedData(input_data)
        
        pd.testing.assert_frame_equal(result, expected_output)

    def test_formatRankedData_missingTraitType(self):
        input_data = {
            "columns": ["Hat", "Mouth"],
            "distributions": [
                {
                    "tokenId": "1",
                    "totalScoreDistribution": [
                        {
                            "traitType": "Hat",
                            "score": 2
                        }
                    ]
                },
                {
                    "tokenId": "2",
                    "totalScoreDistribution": [
                        {
                            "traitType": "Mouth",
                            "score": 1
                        }
                    ]
                }
            ]
        }

        expected_output = pd.DataFrame(columns=['Hat', 'Mouth'], index=['1', '2'])
        expected_output.index.name = 'tokenId'
        expected_output.iloc[0] = [2, 0]
        expected_output.iloc[1] = [0, 1]

        result = formatRankedData(input_data)

        pd.testing.assert_frame_equal(result, expected_output)
    
    def test_formatRankedData_multipleTraitOccurrences(self):
        input_data = {
            "columns": ["Hat"],
            "distributions": [
                {
                    "tokenId": "1",
                    "totalScoreDistribution": [
                        {
                            "traitType": "Hat",
                            "score": 1
                        },
                        {
                            "traitType": "Hat",
                            "score": 2
                        }
                    ]
                }
            ]
        }

        expected_output = pd.DataFrame(columns=['Hat','Hat'], index=['1'])
        expected_output.index.name = 'tokenId'
        expected_output.iloc[0] = [1, 2]
    
        result = formatRankedData(input_data)

        pd.testing.assert_frame_equal(result, expected_output)

if __name__ == "__main__":
    unittest.main()