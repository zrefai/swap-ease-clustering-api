import time
from src.helpers.dateHelpers import getDateBoundary
from src.apis.openSea.eventsService import EventsService
from src.helpers.getEnvVariables import getEnvVariables

class EventsClass:
    envVariables = getEnvVariables()

    def __init__(self):
        self.eventsService = EventsService()
        self.dateRange = 90

    def getEvents(self, contractAddress, latestEventTimestamp = None):
        dateBoundary = getDateBoundary(self.dateRange)

        # Unix epoch time for events that occurred after this calculated time
        # Check if latestEventTimestamp is past 90 day range from now
        if latestEventTimestamp is not None and latestEventTimestamp > dateBoundary:
            occurredAfter = latestEventTimestamp.timestamp()
        else:
            occurredAfter = dateBoundary.timestamp()
    
        url = self.urlBuilder(contractAddress, occurredAfter)
        headers = {
            'accept': 'application/json',
            'X-API-KEY': self.envVariables['OPENSEA_API_KEY']
        }

        response = self.eventsService.getEvents(url, headers)
        events = self.__mergeBuckets({}, response['assetEvents'])

        while response['next'] is not None:
            time.sleep(0.8)

            url = self.urlBuilder(contractAddress, occurredAfter, response['next'])
            response = self.eventsService.getEvents(url, headers)
            events = self.__mergeBuckets(events, response['assetEvents'])
        
        return events
    
    def urlBuilder(self, contractAddress, timestamp, cursor = None):
        openseaUrl = self.envVariables['OPENSEA_URL']

        assetContractAddress = 'asset_contract_address={0}'.format(contractAddress)
        eventType = 'event_type=successful'
        occurredAfter = 'occurred_after={0}'.format(timestamp)

        if cursor:
            nextCursor = 'cursor={0}'.format(cursor)

            return '{0}/events?{1}&{2}&{3}&{4}'.format(
            openseaUrl, 
            assetContractAddress, 
            eventType, 
            occurredAfter,
            nextCursor)

        return '{0}/events?{1}&{2}&{3}'.format(
            openseaUrl, 
            assetContractAddress, 
            eventType, 
            occurredAfter)
    
    def __mergeBuckets(self, currBuckets, assetEvents):
        newBuckets = self.__bucketEventsByTokenId(assetEvents)

        for tokenId in newBuckets.keys():
            if tokenId in currBuckets:
                currBuckets[tokenId] += newBuckets[tokenId]
            else:
                currBuckets[tokenId] = newBuckets[tokenId]

        return currBuckets
    
    def __bucketEventsByTokenId(self, assetEvents):
        buckets = {}

        for event in assetEvents:
            if event['tokenId'] in buckets:
                buckets[event['tokenId']].append(event)
            else:
                buckets[event['tokenId']] = [event]
    
        return buckets