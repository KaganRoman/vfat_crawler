import argparse

from config import Blockchain
from browsers.browser import Browser
from db.db import Database
from parsers.vfat import Vfat


INCLUDE_LIST = {
    Blockchain.ETH: [],
    Blockchain.BSC: [],
    Blockchain.HECO: ['https://vfat.tools/heco/lava/']     
}


def parse_blockchain(blockchain):
    db = Database(blockchain)
    browser = Browser(blockchain)
    with browser:
        results = Vfat(blockchain).extract(browser, INCLUDE_LIST[blockchain])
        db.add(results)
        
    
if __name__ == '__main__':
    my_parser = argparse.ArgumentParser(description='Parse yields')

    # Add the arguments
    my_parser.add_argument('-b', '--blockchain', action='store', choices=[*Blockchain.list(), 'all'], default='HECO')

    # Execute the parse_args() method
    args = my_parser.parse_args()

    for b in Blockchain.list():
        if not args.blockchain in (b, 'all'):
            continue
        parse_blockchain(b)    