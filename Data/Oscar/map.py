#!/usr/bin/python

import sys
import string

for line in sys.stdin:
    line = line.strip().split('\t')
    print '%s,%s'%(line[0],line[1])
