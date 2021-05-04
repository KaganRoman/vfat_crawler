"""Constants that can be changed"""

# Must ne at the same folder with parse_site.py
PATH_TO_METAMASK_EXTENSION_CRX_FILE = 'extension_9_4_0_0.crx' 

TIMEOUT_FOR_CONTRACTS_PAGE_LOADING = 60
TIMEOUT_FOR_VERBOSE_PAGE_LOADING = 60


TIMEOUT_FOR_AUTORIZATION_PAGE_LOADING = 60
REDUCED_TIMEOUT_FOR_AUTORIZATION_PAGE_LOADING = 3

# Password for metamask, doesnt need to be changed
PASSWORD_FOR_METAMASK = 'hellokitty'


ETH_ADDRESS = 'https://vfat.tools'
BSC_ADDRESS = 'https://vfat.tools/bsc'
HECO_ADDRESS = 'https://vfat.tools/heco'

ETH_NAME = 'ETH'
BSC_NAME = 'BSC'
HECO_NAME = 'HECO'


# Csv columns names, can be changed
HEADERS = ['Blockchain', 'Protocol', 'Token 0', 'Token 1', 'APR', 'Staked']

# Phrase after which smart contracts list begins
BORDER_PHRASE = "Finished reading smart contracts.\n"

# Phrase which appears at the end of the page with smart contracts. Need to indicate that page was fully loaded
TOTAL_STAKED = 'Total'

STAKED = 'Staked'

# Phrase which appears at the end of the page with various links. Need to indicate that page was fully loaded
DISCLAIMER = 'Disclaimer'

APPEND_MODE = 'a'

NUMBER_OF_REFRESH_TRIES = 3

