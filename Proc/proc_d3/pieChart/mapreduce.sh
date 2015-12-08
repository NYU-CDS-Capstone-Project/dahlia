#!/bin/sh
chmod 777 *.py
cat ../../../Data/Oscar/hashtagCount | ./map.py > ../../../Vis/data_o/hashCount.csv
cat ../../../Data/Oscar/sourceCount | ./map.py > ../../../Vis/data_o/sourceCount.csv
cat ../../../Data/Oscar/locationCount | ./map.py > ../../../Vis/data_o/locaCount.csv
cat ../../../Data/Oscar/mentionCount | ./map.py > ../../../Vis/data_o/userCount.csv

cat ../../../Data/Hillary/result_coord.txt | ./mapcoord.py | sort | ./reduce.py > ../../../Vis/data/stateCount.csv
