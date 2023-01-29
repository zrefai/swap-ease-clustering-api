import time
from src.apis.openSea.eventsService import EventsService
from src.helpers.getEnvVariables import getEnvVariables

class EventsClass:
    envVariables = getEnvVariables()

    def __init__(self):
        self.eventsService = EventsService()
        self.dateRange = 90

    def getOldEvents(self, contractAddress):
        currentTime = time.time()
    
        # Unix epoch time for events that occurred after this calculated time
        occuredAfter = currentTime - (86400*self.dateRange)
    
        url = self.urlBuilder(contractAddress, occuredAfter)
        headers = {
            'accept': 'application/json',
            'X-API-KEY': self.envVariables['OPENSEA_API_KEY']
        }

        response = self.eventsService.getEvents(url, headers)

        events = self.__mergeBuckets({}, response['assetEvents'])

        while response['next'] is not None:
            time.sleep(0.8)

            url = self.urlBuilder(contractAddress, occuredAfter, response['next'])
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