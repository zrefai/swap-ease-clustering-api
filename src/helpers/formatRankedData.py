import pandas as pd
from data.collectionNfts.collectionNftsDataClasses import CollectionData


def formatRankedData(collectionData: CollectionData) -> pd.DataFrame:
    columnsCount: dict[str, int] = {}

    # Get the max number of occurances of a trait across all NFTs
    for column in collectionData.columns:
        for collectionNFT in collectionData.collectionData:
            result = [attribute for attribute in collectionNFT.attributeScores
                      if attribute.traitType == column]

            if column in columnsCount:
                columnsCount[column] = max(columnsCount[column], len(result))
            else:
                columnsCount[column] = len(result)

    dataFrameColumns: list[str] = []

    # Create columns list for data frame with max occurances accounted for
    for k in columnsCount:
        for i in range(1, columnsCount[k] + 1):
            dataFrameColumns.append(k)

    # Get list of indexes by tokenId
    indexes = [collectionNFT.tokenId
               for collectionNFT in collectionData.collectionData]

    # Create data frame with columns and tokenIds as indexes
    dataFrame = pd.DataFrame(columns=[*dataFrameColumns], index=indexes)
    dataFrame.index.name = 'tokenId'

    # Loop through data frame columns to fill in data from attribute scores
    for index, token in enumerate(dataFrame.index):
        row = []

        # Format data per row
        for key in columnsCount:
            result = [attribute.score for attribute in collectionData.collectionData
                      [index].attributeScores if attribute.traitType == key]

            # Fill remaining columns of a trait type with 0s if no other data is available
            while len(result) < columnsCount[key]:
                result.append(0)

            row += result

        # Fill entire row of data frame with newly formatted row
        dataFrame.loc[token] = row

    return dataFrame
