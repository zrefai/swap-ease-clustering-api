from mongoDb import get_db

class SortedRankings():
    def __init__(self):
        db = get_db()

        self.collection = db['sortedRankings']
    
    def getSortedRankings(self, contractAddress):
        # Get sortedRanking document
        document = self.collection.find_one({'contractAddress': contractAddress})

        def mapScores(a):
            return {
                'trait_type': a['trait_type'],
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
