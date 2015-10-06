#!/bin/sh
zcat *.gz |./jq '[.id, .text]' -c | |./lmr 5m 16 'python ../proc/generateName.py' 'python ../proc/count.py' result_test

