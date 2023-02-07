import requests
from src.helpers.dateHelpers import getDateObject

class EventsService:    
    def getEvents(self, url, headers):
        # TODO: Do more error handling here
        response = requests.get(url, headers=headers)
        
        if response.ok:
            return self.__eventsMapper(response.json())

        return {
            'next': None,
            'assetEvents': []
        }
    
    def __eventsMapper(self, response):
        def mapEvent(e):
            return {
                'tokenId': e['asset']['token_id'],
                'eventTimestamp': getDateObject( e['event_timestamp']),
                'totalPrice': e['total_price'],
                'paymentToken': e['payment_token']['symbol']
            }
    
        return {
            'next': response['next'],
            'assetEvents': list(map(mapEvent, response['asset_events']))
        }