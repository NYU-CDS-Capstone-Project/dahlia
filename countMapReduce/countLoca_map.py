#!/usr/bin/env python

import json
import sys
import string
import nltk
import goose
from pprint import pprint
import collections
import matplotlib.pyplot as plt
import numpy as np
import os
# %matplotlib inline
# import shlex, subprocess

lineCount = 0

for line in sys.stdin:
	lineCount += 1
	try:
		l = json.loads(line)
		loca = str(l['user']['location'])
	except:
		pass
	if loca != '':
		print "%s|%d" % (loca, 1)	

# print lineCount