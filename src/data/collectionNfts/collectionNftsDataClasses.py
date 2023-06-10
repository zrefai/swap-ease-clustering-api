from dataclasses import dataclass


@dataclass
class Attribute:
    traitType: str
    score: float


@dataclass
class CollectionNFT:
    tokenId: str
    rank: int
    attributeScores: list[Attribute]


@dataclass
class CollectionData:
    columns: list[str]
    collectionData: list[CollectionNFT]
