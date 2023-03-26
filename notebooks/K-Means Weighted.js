// Helper function to calculate weighted Euclidean distance between two points
function weightedEuclideanDistance(point1, point2, weights) {
  let distance = 0;
  for (const key in point1) {
    distance += Math.pow((point1[key] - point2[key]) * weights[key], 2);
  }
  return Math.sqrt(distance);
}

// Modified k-means clustering algorithm with attribute weights
function weightedKMeansClustering(
  nftCollection,
  attributeWeights,
  k = 3,
  maxIterations = 100
) {
  const centroids = nftCollection
    .slice(0, k)
    .map((nft) => ({ ...nft.normalizedAttributes }));

  for (let i = 0; i < maxIterations; i++) {
    const clusters = Array.from({ length: k }, () => []);

    for (const nft of nftCollection) {
      const distances = centroids.map((centroid) =>
        weightedEuclideanDistance(
          nft.normalizedAttributes,
          centroid,
          attributeWeights
        )
      );
      const clusterIndex = distances.indexOf(Math.min(...distances));
      clusters[clusterIndex].push(nft);
    }

    let newCentroids = clusters.map(calculateCentroid);
    newCentroids = newCentroids.filter((centroid) => centroid !== null);

    if (newCentroids.length !== k) {
      const randomNFTs = nftCollection
        .sort(() => 0.5 - Math.random())
        .slice(0, k);
      newCentroids = randomNFTs.map((nft) => ({ ...nft.normalizedAttributes }));
    }

    centroids.length = 0;
    centroids.push(...newCentroids);
  }

  return centroids.map((centroid, index) => ({
    centroid,
    cluster: nftCollection.filter(
      (nft) =>
        weightedEuclideanDistance(
          nft.normalizedAttributes,
          centroid,
          attributeWeights
        ) ===
        Math.min(
          ...centroids.map((c) =>
            weightedEuclideanDistance(
              nft.normalizedAttributes,
              c,
              attributeWeights
            )
          )
        )
    ),
  }));
}

// Normalize attributes and calculate weighted rarity score for each NFT
const nftCollectionWithNormalizedAttributes = nftCollection.map((nft) => ({
  ...nft,
  normalizedAttributes: normalizeAttributes(nft.attributes),
}));

// Perform weighted k-means clustering on the NFT collection
const clusters = weightedKMeansClustering(
  nftCollectionWithNormalizedAttributes,
  attributeWeights,
  3
);
console.log(clusters);
