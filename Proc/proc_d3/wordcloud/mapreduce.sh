#!/bin/sh
chmod 777 *.py
cat ../../../Data/Oscar/retweetCount | ./countWord_map.py | sort | ./countWord_reduce.py > ../../../Vis/data_o/wordCount.txt

