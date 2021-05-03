import pytest

from vfat_crauler import extract_contract_values

test_input1 = ("""
'\n[Lava]-[USDT] Uni LP [+] [-] [<=>] Price: $1.28 TVL: $719,789.77\nLava Price: $0.33\nUSDT Price: $1.00\nStaked: 555788.7282 LavaSwap ($713,407.80)\nLAVA Per Week: 115068.49 ($38,378.34)\nAPR: Day 0.77% Week 5.38% Year 279.74%\nYou are staking 0.00 [Lava]-[USDT] Uni LP ($0.00), 0.00% of the pool.\nStake 0.00 [Lava]-[USDT] Uni LP\nUnstake 0.00 [Lava]-[USDT] Uni LP\nClaim 0.00 LAVA ($0.00)\nStaking or unstaking also claims rewards.'
""",
'Lava',
'USDT',
'279.74',
'713,407.80'
)


TEST_INPUTS=[test_input1]

@pytest.mark.parametrize('ts', TEST_INPUTS)
def test_extract_contract_values(ts):
    name_1, name_2, apr, staked = extract_contract_values(ts[0])
    assert name_1 == ts[1]
    assert name_2 == ts[2]
    assert apr == ts[3]
    assert staked == ts[4]
