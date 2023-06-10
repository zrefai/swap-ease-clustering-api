import requests
from helpers.dateHelpers import getDateObject


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
        assetEvents = []

        for event in response['asset_events']:
            if event['asset'] is not None:
                assetEvents.append({
                    'tokenId': event['asset']['token_id'],
                    'eventTimestamp': getDateObject(event['event_timestamp']),
                    'totalPrice': event['total_price'],
                    'paymentToken': event['payment_token']['symbol'],
                    'bundled': False
                })

            # TODO: handle bundled events
            # elif event['asset_bundle'] is not None:
            #     for bundledAsset in event['asset_bundle']['assets']:
            #         assetEvents.append({
            #             'tokenId': bundledAsset['token_id'],
            #             'eventTimestamp': getDateObject(event['event_timestamp']),
            #             'totalPrice': str(int(event['total_price']) / len(event['asset_bundle']['assets'])),
            #             'paymentToken': event['payment_token']['symbol'],
            #             'bundled': True
            #         })

        return {
            'next': response['next'],
            'assetEvents': assetEvents
        }
