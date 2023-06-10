from dataclasses import dataclass


@dataclass
class Fee:
    amount: str
    tokenAddress: str
    symbol: str
    decimals: int


@dataclass
class NFTEvent:
    marketplace: str
    contractAddress: str
    tokenId: str
    sellerFee: Fee
    protocolFee: Fee
    royaltFee: Fee
    blockNumber: int
    blockTimestamp: str


@dataclass
class GetEvents:
    pageKey: str | None
    events: list[NFTEvent]
