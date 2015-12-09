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

hashtag = ''

for line in sys.stdin:
	# lineCount += 1
	try:
		l = json.loads(line)
		hashtag = str(l['entities']['hashtags'][0]['text'])
	
	except:
		continue
	
	if hashtag != '':
		print "%s\t%d" % (hashtag, 1)
