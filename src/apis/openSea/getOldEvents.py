import time
from apis.openSea.eventsHandler import eventsHandler
from helpers.getEnvVariables import getEnvVariables

envVariables = getEnvVariables()

DATE_RANGE = 90

def getOldEvents(contractAddress):
    currentTime = time.time()
    
    # Unix epoch time for events that occurred after this calculated time
    occuredAfter = currentTime - (86400*DATE_RANGE)
    
    url = urlBuilder(contractAddress, occuredAfter)
    headers = {
        "accept": "application/json",
        "X-API-KEY": envVariables['OPENSEA_API_KEY']
    }

    response = eventsHandler(headers, url)
    events = mergeBuckets({}, response["assetEvents"])

    while response["next"] is not None:
        time.sleep(0.8)

        url = urlBuilder(contractAddress, occuredAfter, response["next"])
        response = eventsHandler(headers, url)
        events = mergeBuckets(events, response["assetEvents"])
        
    return events

def bucketEventsByTokenId(assetEvents):
    buckets = {}

    for event in assetEvents:
        if event["tokenId"] in buckets:
            buckets[event["tokenId"]].append(event)
        else:
            buckets[event["tokenId"]] = [event]
    
    return buckets

def mergeBuckets(currBuckets, assetEvents):
    newBuckets = bucketEventsByTokenId(assetEvents)

    for tokenId in newBuckets.keys():
        if tokenId in currBuckets:
            currBuckets[tokenId] += newBuckets[tokenId]
        else:
            currBuckets[tokenId] = newBuckets[tokenId]

    return currBuckets


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
