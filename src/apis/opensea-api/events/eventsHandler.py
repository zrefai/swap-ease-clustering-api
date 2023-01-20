import requests
import json

def eventsHandler(headers, url):
    response = requests.get(url, headers=headers)

    if response.ok:
        return eventsMapper(json.loads(response.json()))
    pass

def eventsMapper(response):
    pass