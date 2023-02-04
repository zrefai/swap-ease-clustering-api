from typing import Any
from src.mongoDb import get_db

class SortedRankings():
    def __init__(self):
        db = get_db()

        self.collection = db['sortedRankings']
    
    def getSortedRankings(self, contractAddress) -> dict[str, Any]:
        try:
            document = self.collection.find_one({'contractAddress': contractAddress})

            if document is None:
                raise TypeError('SortedRanking document for {} was not found'.format(contractAddress))

            def mapScores(a):
                return {
                    'traitType': a['trait_type'],
                    'score': a['score']
                }

            def mapRankings(r):
                scores = list(map(mapScores, r['metadata']['attributes']))
                return {
                    'tokenId': r['tokenId'],
                    'totalScoreDistribution': scores
                }

            distributions = list(map(mapRankings, document['sortedRanking']))
            columns = list(map(lambda a: a['trait_type'], document['sortedRanking'][0]['metadata']['attributes']))

            return {
                'columns': columns,
                'distributions': distributions
            }
        except TypeError as e:
            # TODO: Use a logger here
            print(e)

            raise Exception('Cannot continue without SortedRanking data') from e
