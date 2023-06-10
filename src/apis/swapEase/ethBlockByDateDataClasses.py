from dataclasses import dataclass

@dataclass
class EthBlockByDate:
    date: str
    block: int
    timestamp: int