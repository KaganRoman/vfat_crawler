import pytest

from vfat_crauler import extract_contract_values
from inputs_test import TEST_INPUTS


@pytest.mark.parametrize('ts', TEST_INPUTS)
def test_extract_contract_values(ts):
    name_1, name_2, apr, staked = extract_contract_values(ts[0])
    assert name_1 == ts[1]
    assert name_2 == ts[2]
    assert apr == ts[3]
    assert staked == ts[4]
