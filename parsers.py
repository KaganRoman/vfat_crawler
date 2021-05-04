from enum import Enum
import re
import logging


from constants import STAKED


class ContractNamePattern(Enum):
    VARIANT_1 = r"\[(.*?)\]-\[(.*?)\]"
    VARIANT_2 = r"\w+ Price:"


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


def extract_contract_values(contract, address=None, various_link=None):
    name_1, name_2 = find_name_by_pattern(contract)
    if name_1 is None:
        logging.error(f'Address = {address}, various_link = {various_link}. '
                      f'Did not catch name from contract = {contract}')
        return None, None, None, None

    contract_apr = find_apr_by_pattern(contract)
    if contract_apr is None:
        logging.error(f'Address = {address}, various_link = {various_link}. '
                      f'Did not catch apr from contract = {contract}')
        return None, None, None, None

    contract_staked = find_staked_by_pattern(contract)
    if contract_staked is None:
        logging.error(f'Address = {address}, various_link = {various_link}. '
                      f'Did not catch staked from contract = {contract}')
        return None, None, None, None

    return name_1, name_2, contract_apr, contract_staked

