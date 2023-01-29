import pandas as pd

def formatRankedData(rankedData):
    columnsCount = {}

    # Get the max number of occurances of a trait across all NFTs
    for column in rankedData['columns']:
        for distribution in rankedData['distributions']:
            result = [x for x in distribution['totalScoreDistribution'] if x['trait_type'] == column]
        
            if column in columnsCount:
                columnsCount[column] = max(columnsCount[column], len(result))
            else:
                columnsCount[column] = len(result)

    # Create columns list for data frame with max occurances accounted for
    dataFrameColumns = []
    for k in columnsCount:
        for i in range(1, columnsCount[k] + 1):
            dataFrameColumns.append(k)

    # Get list of indexes by tokenId
    indexes = [distribution['tokenId'] for distribution in rankedData['distributions']]

    # Create data frame with columns and tokenIds as indexes
    dataFrame = pd.DataFrame(columns=[*dataFrameColumns], index=indexes)
    dataFrame.index.name = 'tokenId'

    # Loop through data frame columns to fill in data from opened file
    for index, token in enumerate(dataFrame.index):
        row = []

        # Format data per row
        for key in columnsCount:
            result = [x['score'] for x in rankedData['distributions'][index]['totalScoreDistribution'] if x['trait_type'] == key]

            # Fill remaining columns of a trait type with 0s if no other data is available
            while len(result) < columnsCount[key]:
                result.append(0)
        
            row += result

        # Fill entire row of data frame with newly formatted row
        dataFrame.loc[token] = row

    return dataFrame