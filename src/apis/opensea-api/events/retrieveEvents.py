import time
from helpers.getEnvVariables import getEnvVariables

envVariables = getEnvVariables()

DATE_RANGE = 90

def retrieveOldEvents(contractAddress):
    currentTime = time.time()
    
    # Unix epoch time for events that occurred after this calculated time
    occuredAfter = currentTime - (86400*DATE_RANGE)
    
    url = urlBuilder(contractAddress, occuredAfter)

    headers = {
        "accept": "application/json",
        "X-API-KEY": envVariables['OPENSEA_API_KEY']
    }

    events = []

    pass


def urlBuilder(contractAddress, timestamp, cursor = None):
    openseaUrl = envVariables['OPENSEA_URL']

    assetContractAddress = "asset_contract_address={0}".format(contractAddress)
    eventType = "event_type=successful"
    occurredAfter = "occurred_after={0}".format(timestamp)

    if cursor:
        nextCursor = "cursor={0}".format(cursor)

        return "{0}/events?{1}&{2}&{3}&{4}".format(
        openseaUrl, 
        assetContractAddress, 
        eventType, 
        occurredAfter,
        nextCursor)

    return "{0}/events?{1}&{2}&{3}".format(
        openseaUrl, 
        assetContractAddress, 
        eventType, 
        occurredAfter)
