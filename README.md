# forkstats
Code to be determining how long it would take to be recovering from large loss of mining power on bitcoin chain.

Results are in results.txt and can be computed still again as

python forkstats.py > results.txt

Green: blocktimes <= 12 mins
Yellow: blocktimes > 12 mins & <= 20 mins
Amber: blocktimes > 20 mins & <= 30 mins
Red: blocktimes > 30 mins

2 eventualities:

Red; diff adj; then Yellow; diff adj; then Green
Red; diff adj; then Green
