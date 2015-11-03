#!/usr/bin/python

import sys
import string

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    try:
        line = line.strip()
        l = line.split('\t')
        for word in l:
            print "%s,%d" %(l[0],int(l[1]))
    except:
        pass
