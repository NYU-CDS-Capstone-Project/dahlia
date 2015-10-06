#!/bin/sh
cat 2014_03_02_23_00_05.json |./jq '.text'

python <<@@
print 'hello from Python!'
@@
