#!/usr/bin/env python

import json
import sys
import string
import os

current_word = None
current_count = 0
word = None

for line in sys.stdin:
	try:	
		word, count = line.split('\t')
		try:
			count = int(count)
		except ValueError:
			continue

		if current_word == word:
			current_count += count
		else:
			if current_word:
				print '%s\t%s' % (current_word, current_count)
			current_count = count
			current_word = word
	except:
		continue

if current_word == word:
	print '%s\t%s' % (current_word, current_count)