"""Constants that can be changed"""

# Must ne at the same folder with parse_site.py
PATH_TO_METAMASK_EXTENSION_CRX_FILE = 'extension_9_4_0_0.crx' 

TIMEOUT_FOR_CONTRACTS_PAGE_LOADING = 60

TIMEOUT_FOR_AUTORIZATION_PAGE_LOADING = 60


# Password for metamask, doesnt need to be changed
PASSWORD_FOR_METAMASK = 'hellokitty' 

VFAT_ADDRESS = 'https://vfat.tools'
BSC_ADDRESS = 'https://vfat.tools/bsc'
HECO_ADDRESS = 'https://vfat.tools/heco'

VFAT_NAME = 'ETH'
BSC_NAME = 'BSC'
HECO_NAME = 'HECO'


CONTRACT_NAME_PATTERN_1 = r"\[([A-Za-z0-9_]+)\]-\[([A-Za-z0-9_]+)\]"
CONTRACT_NAME_PATTERN_2 = r"\w+ Price:"

CONTRACT_APR_PATTERN_1 = r"Year \d+\.\d+\%"
CONTRACT_APR_PATTERN_2 = r"Year \w+%"

# Csv columns names, can be changed
HEADERS = ['Blockchain', 'Protocol', 'Token 0', 'Token 1', 'APR']


