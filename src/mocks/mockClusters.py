import json
def mockClusters():
    f = open('/Users/zakirefai/Work/SwapEase/swap-ease-clustering-api/src/mocks/clusters.json' )
    data = json.load(f)

    return data