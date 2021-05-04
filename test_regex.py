import pytest

from parsers import extract_contract_values, parse_contracts
from inputs_test import TEST_INPUTS
from inputs_pages_test import TEST_PAGES


@pytest.mark.parametrize('ts', TEST_INPUTS)
def test_extract_contract_values(ts):
    name_1, name_2, apr, staked = extract_contract_values(ts[0])
    assert name_1 == ts[1]
    assert name_2 == ts[2]
    assert apr == ts[3]
    assert staked == ts[4]


@pytest.mark.parametrize('contract', TEST_PAGES)
def test_extract_contract_pages(contract):
    rows = parse_contracts(contract[0], None, None, None, None)
    assert len(rows) == contract[1]
