TEST_INPUTS = [
(
"""
'\n[Lava]-[USDT] Uni LP [+] [-] [<=>] Price: $1.28 TVL: $719,789.77\nLava Price: $0.33\nUSDT Price: $1.00\nStaked: 555788.7282 LavaSwap ($713,407.80)\nLAVA Per Week: 115068.49 ($38,378.34)\nAPR: Day 0.77% Week 5.38% Year 279.74%\nYou are staking 0.00 [Lava]-[USDT] Uni LP ($0.00), 0.00% of the pool.\nStake 0.00 [Lava]-[USDT] Uni LP\nUnstake 0.00 [Lava]-[USDT] Uni LP\nClaim 0.00 LAVA ($0.00)\nStaking or unstaking also claims rewards.'
""",
'Lava',
'USDT',
'279.74',
'713,407.80'
),

(
"""
[HBTC]-[USDT] Uni LP [+] [-] [<=>] Price: $479.66 TVL: $333,580,720.46\nHBTC Price: $57,488.00\nUSDT Price: $1.00\nStaked: 695122.2576 HMDX ($333,420,748.75)\nMDX Per Week: 567897.12 ($1,817,270.78)\nAPR: Day 0.08% Week 0.55% Year 28.34%\nYou are staking 0.00 [HBTC]-[USDT] Uni LP ($0.00), 0.00% of the pool.\nStake 0.00 [HBTC]-[USDT] Uni LP\nUnstake 0.00 [HBTC]-[USDT] Uni LP\nClaim 0.00 MDX ($0.00)\nStaking or unstaking also claims rewards.
""",
'HBTC',
'USDT',
'28.34',
'333,420,748.75'
),

(
"""
[COM+]-[USDT] Uni LP [+] [-] [<=>] Price: $0.25 TVL: $34,997.54\nCOM+ Price: $0.02\nUSDT Price: $1.00\nStaked: 137375.5496 COM-LP ($34,956.93)\nCOM Per Week: 120960.00 ($1,922.92)\nAPR: Day 0.79% Week 5.50% Year 286.04%\nYou are staking 0.00 [COM+]-[USDT] Uni LP ($0.00), 0.00% of the pool.\nStake 0.00 [COM+]-[USDT] Uni LP\nUnstake 0.00 [COM+]-[USDT] Uni LP\nClaim 0.00 COM ($0.00)\nStaking or unstaking also claims rewards.
""",
'COM+',
'USDT',
'286.04',
'34,956.93'
),

(
"""
bofHBTC Price: $1,154.72 Market Cap: $39,646,294.18\nStaked: 34027.9932 bofHBTC ($39,292,804.31)\nBOO Per Week: 88271.74 ($91,689.16)\nAPR: Day 0.03% Week 0.23% Year 12.13%\nYou are staking 0.00 bofHBTC ($0.00), 0.00% of the pool.\nStake 0.00 bofHBTC\nUnstake 0.00 bofHBTC\nClaim 0.00 BOO ($0.00)\nStaking or unstaking also claims rewards.
""",
'bofHBTC',
'',
'12.13',
'39,292,804.31'
),

(
"""
PIPI Price: $1.43 Market Cap: $76,998,421.05\nStaked: 17600052.1411 PIPI ($25,200,067.62)\nPIPI Per Week: 1007958.06 ($1,443,212.27)\nAPR: Day 0.82% Week 5.73% Year 297.80%\nYou are staking 0.00 PIPI ($0.00), 0.00% of the pool.\nStake 0.00 PIPI\nUnstake 0.00 PIPI\nClaim 0.00 PIPI ($0.00)\nStaking or unstaking also claims rewards.
""",
'PIPI',
'',
'297.80',
'25,200,067.62'
),
(
"""
[FARM]-[USDC] Uni LP [+] [-] [<=>] Price: $31,044,900.51 TVL: $231,230.19\nFARM Price: $171.21\nUSDC Price: $1.00\nStaked: 0.0024 UNI-V2 ($73,978.60)\nFARM Per Week: 0.00 ($0.00)\nAPR: Day 0.00% Week 0.00% Year 0.00%\nYou are staking 0.00 [FARM]-[USDC] Uni LP ($0.00), 0.00% of the pool.\nStaking Contract\nStake 0.000000 [FARM]-[USDC] Uni LP\nUnstake 0.000000 [FARM]-[USDC] Uni LP\nClaim 0.000000 FARM\nExit
""",
'FARM',
'USDC',
'0.00',
'73,978.60'    
),
(
"""
fWETH Price: $3,388.86 TVL: $20,993,974.46\nStaked: 6133.4881 fWETH ($20,785,561.64)\nFARM Per Week: 62.89 ($10,768.17)\nAPR: Day 0.01% Week 0.05% Year 2.69%\nYou are staking 0.00 fWETH ($0.00), 0.00% of the pool.\nStaking Contract\nStake 0.000000 fWETH\nUnstake 0.000000 fWETH\nClaim 0.000000 FARM\nExit
""",
'fWETH',
'',
'2.69',
'20,785,561.64'
),
(
"""
Wrapped [DPI]-[WETH] Uni LP Price: $3,202.77 TVL: $4,066,862.91\nStaked: 1222.5769 fUNI-V2 ($3,915,633.99)\nFARM Per Week: 11.74 ($2,010.06)\nAPR: Day 0.01% Week 0.05% Year 2.67%\nYou are staking 0.00 fUNI-V2 ($0.00), 0.00% of the pool.\nStaking Contract\nStake 0.000000 fUNI-V2\nUnstake 0.000000 fUNI-V2\nClaim 0.000000 FARM\nExit
""",
'DPI',
'WETH',
'2.67',
'3,915,633.99'    
),
(
"""
fyDAI+yUSDC+yUSDT+yTUSD Price: $1.14 TVL: $1,912,850.22\nStaked: 1539513.9780 fyDAI+yUSDC+yUSDT+yTUSD ($1,752,351.73)\nFARM Per Week: 10.48 ($1,794.69)\nAPR: Day 0.01% Week 0.10% Year 5.33%\nYou are staking 0.00 fyDAI+yUSDC+yUSDT+yTUSD ($0.00), 0.00% of the pool.\nStaking Contract\nStake 0.000000 fyDAI+yUSDC+yUSDT+yTUSD\nUnstake 0.000000 fyDAI+yUSDC+yUSDT+yTUSD\nClaim 0.000000 FARM\nExit
""",
'fyDAI+yUSDC+yUSDT+yTUSD',
'',
'5.33',
'1,752,351.73'    
),
(
"""
Cake Price: $36.70 Market Cap: $10,354,441,754.63\nStaked: 4569819.2680 Cake ($167,712,367.13)\nAUTO Per Week: 28.04 ($100,418.95)\nAPR: Day 0.01% Week 0.06% Year 3.11%\nYou are staking 0.00 Cake ($0.00), 0.00% of the pool.\nStake 0.00 Cake\nUnstake 0.00 Cake\nClaim 0.00 AUTO ($0.00)\nStaking or unstaking also claims rewards.
""",
'Cake',
'',
'3.11',
'167,712,367.13'    
),
(
"""
[WBNB]-[BAKE] Uni LP [+] [-] [<=>] Price: $170.26 TVL: $89,299,875.38\nWBNB Price: $619.77\nBAKE Price: $6.00\nStaked: 11417.3084 BLP ($1,943,965.76)\nAUTO Per Week: 2.80 ($10,041.90)\nAPR: Day 0.07% Week 0.52% Year 26.86%\nYou are staking 0.00 [WBNB]-[BAKE] Uni LP ($0.00), 0.00% of the pool.\nStake 0.00 [WBNB]-[BAKE] Uni LP\nUnstake 0.00 [WBNB]-[BAKE] Uni LP\nClaim 0.00 AUTO ($0.00)\nStaking or unstaking also claims rewards.
""",
'WBNB',
'BAKE',
'26.86',
'1,943,965.76'    
),
(
"""
ibBUSD Price: $1.00 Market Cap: $391,780,242.02\nStaked: 390351857.0437 ibBUSD ($390,351,857.04)\nALPACA Per Week: 518432.87 ($1,513,823.99)\nAPR: Day 0.06% Week 0.39% Year 20.17%\nYou are staking 0.00 ibBUSD ($0.00), 0.00% of the pool.\nStake 0.00 ibBUSD\nUnstake 0.00 ibBUSD\nClaim 0.00 ALPACA ($0.00)\nStaking or unstaking also claims rewards.
""",
'ibBUSD',
'',
'20.17',
'390,351,857.04'    
),
(
"""
[SXP]-[BUSD] SLP [+] [-] [<=>] Price: $4.52 TVL: $3,737,049.13\nSXP Price: $4.87\nBUSD Price: $1.00\nStaked: 816962.9866 SLP ($3,695,947.39)\nSWIPE Per Week: 5121.94 ($24,943.86)\nAPR: Day 0.10% Week 0.67% Year 35.09%\nYou are staking 0.00 [SXP]-[BUSD] SLP ($0.00), 0.00% of the pool.\nStake 0.00 [SXP]-[BUSD] SLP\nUnstake 0.00 [SXP]-[BUSD] SLP\nClaim 0.00 SWIPE ($0.00)\nStaking or unstaking also claims rewards.
""",
'SXP',
'BUSD',
'35.09',
'3,695,947.39'    
),
]