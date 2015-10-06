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
		person = str(l['user']['screen_name'])
	except:
		pass
		person = ''

	if person != '':
		print "%s|%d" % (person, 1)	