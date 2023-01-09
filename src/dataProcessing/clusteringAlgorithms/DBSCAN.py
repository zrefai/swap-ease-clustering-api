from sklearn.cluster import DBSCAN

def getDbscanLabels(embedding):
    clusterer_DBSCAN = DBSCAN(eps=.5)
    labels = clusterer_DBSCAN.fit_predict(embedding)

    return labels