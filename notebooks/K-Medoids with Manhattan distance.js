// Helper function to calculate Manhattan distance between two points
function manhattanDistance(point1, point2) {
  let distance = 0;
  for (const key in point1) {
    distance += Math.abs(point1[key] - point2[key]);
  }
  return distance;
}

// Function to find the medoid of a cluster
function findMedoid(cluster) {
  let medoid = null;
  let minSumDistances = Infinity;

  for (const candidate of cluster) {
    let sumDistances = 0;
    for (const point of cluster) {
      sumDistances += manhattanDistance(
        candidate.normalizedAttributes,
        point.normalizedAttributes
      );
    }

    if (sumDistances < minSumDistances) {
      minSumDistances = sumDistances;
      medoid = candidate;
    }
  }

  return medoid;
}

// Custom k-medoids clustering algorithm using Manhattan distance
function customKMedoidsClustering(nftCollection, k = 3, maxIterations = 100) {
  let medoids = nftCollection.sort(() => 0.5 - Math.random()).slice(0, k);

  for (let i = 0; i < maxIterations; i++) {
    const clusters = Array.from({ length: k }, () => []);

    for (const nft of nftCollection) {
      const distances = medoids.map((medoid) =>
        manhattanDistance(nft.normalizedAttributes, medoid.normalizedAttributes)
      );
      const clusterIndex = distances.indexOf(Math.min(...distances));
      clusters[clusterIndex].push(nft);
    }

    let newMedoids = clusters.map(findMedoid);

    if (newMedoids.every((_, index) => newMedoids[index] === medoids[index])) {
      // Stop iterations if medoids didn't change
      break;
    }

    medoids = newMedoids;
  }

  return medoids.map((medoid, index) => ({
    medoid,
    cluster: nftCollection.filter(
      (nft) =>
        manhattanDistance(
          nft.normalizedAttributes,
          medoid.normalizedAttributes
        ) ===
        Math.min(
          ...medoids.map((m) =>
            manhattanDistance(nft.normalizedAttributes, m.normalizedAttributes)
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

// Perform custom k-medoids clustering on the NFT collection
const clusters = customKMedoidsClustering(
  nftCollectionWithNormalizedAttributes,
  3
);
console.log(clusters);
