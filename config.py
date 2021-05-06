from enum import Enum, auto


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class Blockchain(str, AutoName):
    ETH = auto()
    BSC = auto()
    HECO = auto()


WHITELIST = {
    Blockchain.ETH: ['https://vfat.tools/aave/'],
    Blockchain.BSC: ['https://app.beefy.finance/'],
    Blockchain.HECO: [] 
}
