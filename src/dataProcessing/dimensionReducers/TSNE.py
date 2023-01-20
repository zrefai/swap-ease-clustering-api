from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE

def createUmapEmbedding(dataFrame):
    scaledDataFrame = StandardScaler().fit_transform(dataFrame)
    tsne = TSNE(n_components=2)
    embedding = tsne.fit_transform(scaledDataFrame)

    return embedding