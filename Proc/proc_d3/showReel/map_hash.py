#!/usr/bin/env python

import os
import sys
import json
import pickle


temp = []

print 'start finding coordinates and hashtags...'
for line in sys.stdin:
	parsed = json.loads(line)
	try:
		if len(parsed['entities']['hashtags']) != 0:
			temp.append((parsed['created_at'],[i['text'] for i in parsed['entities']['hashtags']]))

	except:
		continue

pickle.dump(temp,open("data.pkl",'wb'))
