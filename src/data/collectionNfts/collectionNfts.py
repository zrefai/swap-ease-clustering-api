from data.collectionNfts.collectionNftsDataClasses import Attribute, CollectionData, CollectionNFT
from mongoDb import get_db


class CollectionNFTs():
    def __init__(self):
        db = get_db()

        self.collection = db['collectionNFTs']

    def getCollectionData(self, contractAddress: str) -> CollectionData:
        try:
            # Find all documents for smartContractAddress, sort them by startIndex to get proper order of documents based on tokenId
            documents = self.collection.find(
                {'contractAddress': contractAddress}).sort('startIndex', 1)

            if documents is None:
                raise TypeError(
                    'CollectionNFTs documents for {} was not found'.format(contractAddress))

            # A list of all nfts from each document, making up the entire collection
            nfts = []

            # Loop through documents and get all NFTs from them
            for doc in documents:
                nfts += doc['nfts']

            def mapAttributes(a) -> Attribute:
                return Attribute(a['traitType'], a['score'])

            def mapCollectionNFTs(r) -> CollectionNFT:
                attributeScores = list(
                    map(mapAttributes, r['attributes']))

                return CollectionNFT(r['tokenId'], r['rank'], attributeScores)

            # Map over all NFTs in a collection
            collectionData = list(
                map(mapCollectionNFTs, nfts))

            # Get list of traitTypes
            columns = list(map(
                lambda a: a.traitType, collectionData[0].attributeScores))

            return CollectionData(columns, collectionData)

        except TypeError as e:
            # TODO: Use a logger here
            print(e)

            raise Exception(
                'Cannot continue without CollectionData') from e
