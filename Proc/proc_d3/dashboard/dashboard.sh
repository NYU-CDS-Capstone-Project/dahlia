#!/bin/sh
chmod 777 ./map_hash.py
cat ../../*.json | ./map_hash.py
python preprocess.py

# installing reverse_geocoder

