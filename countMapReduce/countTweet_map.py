#!/usr/bin/env python

import json
import sys
import string
import os
# %matplotlib inline
# import shlex, subprocess

# lineCount = 0

for line in sys.stdin:
	# lineCount += 1
	try:
		l = json.loads(line)
		tweet = str(l['retweeted_status']['text'])
	except:
		pass
		tweet = ''

	if tweet != '':
		print "%s|%d" % (tweet, 1)	