#!/bin/sh
chmod 777 *.py
cat ../../../Data/Oscar/retweetCount | ./map.py > ../../../Vis/data_o/result_tweet.txt

