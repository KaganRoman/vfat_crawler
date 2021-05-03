from vfat_crauler import VfatCrauler

from constants import ETH_NAME
from constants import ETH_ADDRESS

from constants import BSC_NAME
from constants import BSC_ADDRESS


from constants import HECO_NAME
from constants import HECO_ADDRESS


def main():
#    vfat_crauler = VfatCrauler(ETH_ADDRESS, ETH_NAME)
#    vfat_crauler.run()

#    bsc_crauler = VfatCrauler(BSC_ADDRESS, BSC_NAME)
#    bsc_crauler.run()

    heco_crauler = VfatCrauler(HECO_ADDRESS, HECO_NAME)
    heco_crauler.run()


if __name__ == '__main__':
    main()
