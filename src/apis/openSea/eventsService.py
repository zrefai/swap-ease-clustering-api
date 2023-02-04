import requests
import datetime
from src.helpers.dateHelpers import getDateObject

datetime.datetime.ut
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
        def getEvent(e):
            return {
                'tokenId': e['asset']['token_id'],
                'eventTimestamp': getDateObject( e['event_timestamp']),
                'totalPrice': e['total_price'],
                'paymentToken': e['payment_token']['symbol']
            }
    
        return {
            'next': response['next'],
            'assetEvents': list(map(getEvent, response['asset_events']))
        }