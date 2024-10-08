from enum import Enum
import re
import logging


# Phrase after which smart contracts list begins
BORDER_PHRASE = "Finished reading smart contracts.\n"

# Phrase which appears at the end of the page with smart contracts. Need to indicate that page was fully loaded
TOTAL_STAKED = 'Total'

STAKED = 'Staked'

# Phrase which appears at the end of the page with various links. Need to indicate that page was fully loaded
DISCLAIMER = 'Disclaimer'


class ContractNamePattern(Enum):
    VARIANT_1 = r"\[(.*?)\]-\[(.*?)\]"
    VARIANT_2 = r"(.*?) Price:"


class AprValuePattern(Enum):
    VARIANT_1 = r"Year \d+\.\d+\%"
    VARIANT_2 = r"Year \w+%"
    VARIANT_3 = r"Year \d+\%"


class StakedValuePattern(Enum):
    VARIANT_1 = r"\$[(\d+\,+\d+)]+(\.\d+)"


def extract_names_from_brackets(names_in_brackets):
    return re.findall(r"\[(.*?)\]", names_in_brackets[0])


def extract_name_from_context(contract_name_in_context):
    return contract_name_in_context[0].replace(' Price:', '')


def extract_apr_from_context(apr_in_context):
    apr = apr_in_context[0].replace('Year ', '')
    apr = apr.replace('%', '')
    return apr


def extract_staked_from_context(staked_in_context):
    staked = staked_in_context[0].replace('$', '')
    return staked


def find_name_by_pattern(contract):
    contract_name_in_brackets = re.search(ContractNamePattern.VARIANT_1.value, contract)
    if contract_name_in_brackets is not None:
        return extract_names_from_brackets(contract_name_in_brackets)

    contract_name_in_context = re.search(ContractNamePattern.VARIANT_2.value, contract)
    if contract_name_in_context is not None:
        contract_name = extract_name_from_context(contract_name_in_context)
        return contract_name, ''

    return None, None


def find_apr_by_pattern(contract):
    apr_in_context = re.search(AprValuePattern.VARIANT_1.value, contract)

    if apr_in_context is None:
        apr_in_context = re.search(AprValuePattern.VARIANT_2.value, contract)

    if apr_in_context is None:
        apr_in_context = re.search(AprValuePattern.VARIANT_3.value, contract)

    if apr_in_context is not None:
        apr = extract_apr_from_context(apr_in_context)
        return apr
    else:
        return None


def find_staked_by_pattern(contract):
    contract = contract.split('\n')
    staked_in_context = None
    for sentence in contract:
        if STAKED in sentence:
            staked_in_context = re.search(StakedValuePattern.VARIANT_1.value, sentence)

    if staked_in_context is None:
        return None
    else:
        return extract_staked_from_context(staked_in_context)


def extract_contract_values(contract, link=None):
    name_1, name_2 = find_name_by_pattern(contract)
    if name_1 is None:
        logging.error(f'Did not catch name from {link}')
        return None, None, None, None

    contract_apr = find_apr_by_pattern(contract)
    if contract_apr is None:
        logging.error(f'Did not catch apr from {link}')
        return None, None, None, None

    contract_staked = find_staked_by_pattern(contract)
    if contract_staked is None:
        logging.error(f'Did not catch staked from {link}')
        return None, None, None, None

    return name_1, name_2, contract_apr, contract_staked


def parse_contracts(contracts, blockchain, protocol, link):
    starting_index = contracts.find(BORDER_PHRASE)
    contracts = contracts[starting_index + len(BORDER_PHRASE):]

    ending_index = contracts.rfind('\n' + TOTAL_STAKED)
    if ending_index != -1:
        contracts = contracts[:ending_index]

    contracts = contracts.split('\n\n')

    rows = []
    for contract in contracts:
        name_1, name_2, contract_apr, contract_staked = extract_contract_values(contract, link)
        if name_1 is None:
            continue

        row_to_write = [blockchain, protocol, name_1, name_2, contract_apr, contract_staked]
        rows.append(row_to_write)
    return rows
