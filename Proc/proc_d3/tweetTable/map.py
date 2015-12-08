#!/usr/bin/env python

import sys
import string
import os

for line in sys.stdin:
    try:
        w,c = line.strip().split('\t')
        c = int(c)
        print "%s|%d"%(w, c)
    except:
        pass
