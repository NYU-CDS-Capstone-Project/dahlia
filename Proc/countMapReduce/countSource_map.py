#!/usr/bin/env python

import json
import sys
import string
import xml
import collections
import os
import re

for line in sys.stdin:
	try:
		l = json.loads(line)
		source = l['source'].encode('ascii', 'ignore')
		source_ = re.sub('<[^<]+?>', '', source)
  
	except:
		continue
	
	print '%s\t%d' % (source_, 1)
