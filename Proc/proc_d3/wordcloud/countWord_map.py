#!/usr/bin/env python

import json
import sys
import string
import os
from nltk.corpus import stopwords

exclude = string.punctuation
stopsEng = list(stopwords.words("english"))
stopsSpa = list(stopwords.words("spanish"))
stops = stopsEng + stopsSpa
for line in sys.stdin:
    l = line.strip().split('\t')
    text = ''.join([i for i in l[0] if i not in exclude]).lower()
    text = text.split()
    text = [word for word in text if word not in stops]
    c = int(l[1])
    for w in text:
        print "%s\t%d"%(w, c)
