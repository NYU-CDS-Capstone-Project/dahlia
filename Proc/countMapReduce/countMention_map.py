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
		mention = l['entities']['user_mentions'][0]['screen_name']
	except:
		pass
	print "%s|%d" % (mention, 1)	

# print lineCount