from pprint import pprint
import time
from apis.alchemy.nftEventsDataClasses import NFTEvent
from apis.alchemy.nftEventsService import NFTEventsService
from apis.swapEase.ethBlockByDateService import EthBlockByDateService
from helpers.dateHelpers import getDateBoundary


class NFTEventsClass:

    def __init__(self):
        self.dateRange = 90
        self.getEthBlockByDateService = EthBlockByDateService()
        self.nftEventsService = NFTEventsService()

    def getEvents(self, contractAddress) -> dict[str, list[NFTEvent]]:
        # Get the date from 90 days ago
        dateBoundary = getDateBoundary(self.dateRange)

        print(dateBoundary.isoformat())

        # Get block from 90 days ago
        blockBoundary = self.getEthBlockByDateService.getDate(
            dateBoundary.isoformat())
        pprint(vars(blockBoundary))

        # Get first request, then loop based on pageKey
        response = self.nftEventsService.getNFTEvents(
            contractAddress, blockBoundary.block)
        events = self.__bucketEventsByTokenId(response.events)

        while response.pageKey is not None:
            time.sleep(0.8)

            response = self.nftEventsService.getNFTEvents(
                contractAddress, blockBoundary.block, response.pageKey)
            self.__addNewEventsToBuckets(events, response.events)
            print(response.pageKey)

        return events

    def __addNewEventsToBuckets(self, currBuckets: dict[str, list[NFTEvent]], events: list[NFTEvent]) -> None:
        for event in events:
            if event.tokenId in currBuckets:
                currBuckets[event.tokenId].append(event)
            else:
                currBuckets[event.tokenId] = [event]

    def __bucketEventsByTokenId(self, events: list[NFTEvent]) -> dict[str, list[NFTEvent]]:
        buckets: dict[str, list[NFTEvent]] = {}

        for event in events:
            if event.tokenId in buckets:
                buckets[event.tokenId].append(event)
            else:
                buckets[event.tokenId] = [event]

        return buckets
