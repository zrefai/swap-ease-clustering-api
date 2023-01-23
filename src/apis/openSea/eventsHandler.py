import requests

def eventsHandler(headers, url):
    response = requests.get(url, headers=headers)

    if response.ok:
        return eventsMapper(response.json())
    else:
        print("Error at {url}")

    return {
        "next": None,
        "asset_events": []
    }

def eventsMapper(response):

    def getEvent(e):
        return {
            "tokenId": e["asset"]["token_id"],
            "eventTimestamp": e["event_timestamp"],
            "totalPrice": e["total_price"],
            "paymentToken": e["payment_token"]["symbol"]
        }
    
    return {
        "next": response["next"],
        "assetEvents": map(getEvent, response["asset_events"])
    }