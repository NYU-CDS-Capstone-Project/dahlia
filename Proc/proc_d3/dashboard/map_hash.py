#!/usr/bin/env python

import os
import sys
import json
import pickle


coordinates = []
hashtag = []

print 'start finding coordinates and hashtags...'
for line in sys.stdin:
        parsed = json.loads(line)
        try:
            if parsed['geo'] != None:
                coordinates.append(tuple(parsed['geo']['coordinates']))
                hashtag.append(parsed['entities']['hashtags'])
        except:
            continue

pickle.dump(coordinates, open('coordinates.pkl','wb'))
pickle.dump(hashtag, open('hashtag.pkl','wb'))


