from sklearn.preprocessing import StandardScaler
import umap

def createUmapEmbedding(dataFrame):
    scaledDataFrame = StandardScaler().fit_transform(dataFrame)
    reducer = umap.UMAP()
    embedding = reducer.fit_transform(scaledDataFrame)

    return embedding