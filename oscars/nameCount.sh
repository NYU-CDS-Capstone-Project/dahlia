#!/bin/sh
cat 2014_03_02_23_00_05.json |./jq '[.id, .text]' -c | ../proc/generateName.py | sort |../proc/count.py

