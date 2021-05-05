import argparse


from vfat_crauler import VfatCrauler
from constants import ETH_NAME, ETH_ADDRESS, BSC_NAME, BSC_ADDRESS, HECO_NAME, HECO_ADDRESS, BLOCKCHAIN_LIST


ETH_RUN_LIST = []
BSC_RUN_LIST = []
HECO_RUN_LIST = []

def main(blockchain):
   if blockchain in ('ETH', 'all'):
      vfat_crauler = VfatCrauler(ETH_ADDRESS, ETH_NAME, ETH_RUN_LIST)
      vfat_crauler.run()

   if blockchain in ('BSC', 'all'):
      bsc_crauler = VfatCrauler(BSC_ADDRESS, BSC_NAME, BSC_RUN_LIST)
      bsc_crauler.run()

   if blockchain in ('HECO', 'all'):
      heco_crauler = VfatCrauler(HECO_ADDRESS, HECO_NAME, HECO_RUN_LIST)
      heco_crauler.run()


if __name__ == '__main__':
   my_parser = argparse.ArgumentParser(description='Parse yields')

   # Add the arguments
   my_parser.add_argument('-b', '--blockchain', action='store', choices=[*BLOCKCHAIN_LIST, 'all'], default='all')

   # Execute the parse_args() method
   args = my_parser.parse_args()
   
   main(args.blockchain)