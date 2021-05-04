from vfat_crauler import VfatCrauler

from constants import ETH_NAME
from constants import ETH_ADDRESS

from constants import BSC_NAME
from constants import BSC_ADDRESS


from constants import HECO_NAME
from constants import HECO_ADDRESS

ETH_RUN_LIST = ['https://vfat.tools/alphadex/', 'https://vfat.tools/badger/', 'https://vfat.tools/bella/', 'https://vfat.tools/frax/', 'https://vfat.tools/harvest-finance/', 'https://vfat.tools/ichi/', 'https://vfat.tools/powerindex/', 'https://vfat.tools/ruler/', 'https://vfat.tools/siren/', 'https://vfat.tools/stabilize/', 'https://vfat.tools/truefi/', 'https://vfat.tools/usf/']

BSC_RUN_LIST = ['https://vfat.tools/bsc/autofarm', 'https://vfat.tools/bsc/bake', 'https://vfat.tools/bsc/soup', 'https://vfat.tools/bsc/kimochi', 'https://vfat.tools/bsc/beluga/', 'https://vfat.tools/bsc/midasdollar', 'https://vfat.tools/bsc/mythic', 'https://vfat.tools/bsc/wault', 'https://vfat.tools/bsc/wantanmee', 'https://vfat.tools/bsc/beefy', 'https://vfat.tools/bsc/duckmoney', 'https://vfat.tools/bsc/deflate', 'https://vfat.tools/bsc/squirrel', 'https://vfat.tools/bsc/uranium', 'https://vfat.tools/bsc/bitblocks', 'https://vfat.tools/bsc/yolodraw']


def main():
    #vfat_crauler = VfatCrauler(ETH_ADDRESS, ETH_NAME)
    #vfat_crauler.run()

    bsc_crauler = VfatCrauler(BSC_ADDRESS, BSC_NAME, BSC_RUN_LIST)
    bsc_crauler.run()

    #heco_crauler = VfatCrauler(HECO_ADDRESS, HECO_NAME)
    #heco_crauler.run()


if __name__ == '__main__':
    main()
