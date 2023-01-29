import json

def mockEvents():
  f = open('/Users/zakirefai/Work/SwapEase/swap-ease-clustering-api/src/mocks/events.json')
  data = json.load(f)
  return data