import json
import sys
import string
import nltk
import goose
from pprint import pprint
import collections
import matplotlib.pyplot as plt
import numpy as np
import shlex, subprocess
from operator import *
import itertools
from proc import *

def getField(data):
    return [i[7] for i in data],[i[4] for i in data],[i[8] for i in data]

def getResult(combine):
    result = {}

    for k,v in itertools.groupby(sorted(combine),key=lambda x:x[0]):
        try:
            #result[k] = (set('group.X.%s' % (x[1][0]) for x in v), max([x[2] for x in v]))
            # result[k] = list(set('group.X.%s' % (x[1][0]) for x in v))
            mentions = []
            stats = []
            for x in v:
                for j in x[1]:
                    mentions.append(j)
                stats.append(x[2])
            if len(mentions) > 0:
                result[k] = (list(set(mentions)),max(stats))
        except:
            continue
    return result

def mention_count(name):
    mentions = []
    for key,value in result.iteritems():
        mentions.append(value[0])
    
    cnt = collections.Counter(itertools.chain(*mentions))
    try:
        return cnt[name]
    except:
        return 1
    
def completeData(result):
    
    data_final = sorted([{'name': 'group.X.%s' % (k), 'imports': ['group.X.%s' % (x) for x in v[0]], "size":mention_count(k)} 
               for k,v in result.iteritems()],key=lambda x: x['size'],reverse=True)[:50]
    mentions=list(itertools.chain(*[i['imports'] for i in data_final]))
    names = [i['name'] for i in data_final]
    missing_node = set(mentions) - (set(names) & set(mentions))
    for i in missing_node:
        data.append({'name':i, 'imports':[], 'size':1})


class hier_bund(data):

	def __init__(self,data):
		self.data = data;

	def process_data(self):
		
		user,mention,stats = getField(self.data)

		# Initial zip of all the data
		combine = zip(user,mention,stats)

		result = getResult(combine)

		data_final = completeData(result)

		with open('hier_bund.json','wb') as f:
		    json.dump(data_final,f)	