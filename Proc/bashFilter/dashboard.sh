#!/bin/sh
chmod 777 ../proc_d3/dashboard/map_hash.py
cat ../../Data/Hillary/*.json | ../proc_d3/dashboard/map_hash.py
python ../proc_d3/dashboard/preprocess.py

# installing reverse_geocoder

