#!/bin/sh
chmod 777 ./map_hash.py
cat ../data/*.json | ./map_hash.py
python preprocess.py
