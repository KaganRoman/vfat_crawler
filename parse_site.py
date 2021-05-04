import argparse


from vfat_crauler import VfatCrauler
from constants import ETH_NAME, ETH_ADDRESS, BSC_NAME, BSC_ADDRESS, HECO_NAME, HECO_ADDRESS


ETH_RUN_LIST = None
BSC_RUN_LIST = None
HECO_RUN_LIST = None

def main(blockchain):
   if blockchain in ('eth', 'all'):
      vfat_crauler = VfatCrauler(ETH_ADDRESS, ETH_NAME, ETH_RUN_LIST)
      vfat_crauler.run()

   if blockchain in ('bsc', 'all'):
      bsc_crauler = VfatCrauler(BSC_ADDRESS, BSC_NAME, BSC_RUN_LIST)
      bsc_crauler.run()

   if blockchain in ('heco', 'all'):
      heco_crauler = VfatCrauler(HECO_ADDRESS, HECO_NAME)
      heco_crauler.run()


if __name__ == '__main__':
   my_parser = argparse.ArgumentParser(description='Parse yields')

   # Add the arguments
   my_parser.add_argument('-b', '--blockchain', action='store', choices=['eth', 'bsc', 'heco', 'all'], default='heco')

   # Execute the parse_args() method
   args = my_parser.parse_args()
   
   main(args.blockchain)