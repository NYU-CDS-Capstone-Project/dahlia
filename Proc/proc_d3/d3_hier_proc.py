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

def getFields(name):
	# countEdge_1: contains list of json objects, where each contains 3 fields: name, user mentioned and statuses count 
	# of the user
	# countEdge_1 is used for the hierarchical bundling visualization

	user = []
	mention = []
	stats = []
	with open(name,'rb') as f:
		for line in f:
			if "user" in line:
				user.append(line.split(':')[1].strip(',\n').strip()[1:-1])
			elif "mentions" in line:
				mention.append(line.split(':')[1].strip(',\n').strip()[1:-1])
			elif "statCount" in line:
				stats.append(int(line.split(':')[1].strip(',\n').strip()))
	return user, mentions, stats


def hier_bundling_data(user,mention,stats):
	# Processing the data ready for the hierarchical-bundling graph
	# detail: http://bl.ocks.org/mbostock/7607999

	# preliminary result of the form: {(user_i,stats_count_i):import_i}
	# the form of dictionairy ensures non-duplicacy
	result = {k:list('group.X.%s' % (x[1]) for x in v) for k,v in itertools.groupby(sorted(zip(zip(user,stats),mention)), key=lambda x: x[0])}

	# data: flat out 'result' into the form: {'name':user, 'imports':mention, 'size':stats_count}
	# can adjust the size of the data by modiying the range of k[1] (stats_count) since the d3 limits the 
	# size of the data passed
	data = [{'name': 'group.X.%s' % (k[0]), 'imports': v, "size":k[1]} for k,v in result.items() if k[1] > 1080500]

	mentions=list(itertools.chain(*[i['imports'] for i in data]))
	names = [i['name'] for i in data]
	# missing_node: list of 'node' (user) that appear in the imports but are not an user node in the data
	missing_node = set(mentions) - (set(names) & set(mentions))

	# Append the missing nodes into the data as an empty node (does not import other nodes)
	# To avoid the undefined issue raised in d3
	for i in missing_node:
		data.append({'name':i, 'imports':[], 'size':1})
	return data


if __name__ == '__main__':
	f = '../bashFilter/countEdge_1'
	user, mention, stats = getFields(f)
	# Constructing the data of the format for hierarchical bundling graph
	# {"name": user, "imports": mention, "size": }

	# data for the hierarchical bundling graph
	data_hierBundling = hier_bundling_data(user,mention,stats)
	with open('data_hierBund.json','wb') as f:
		json.dump(f, '../../Data/Hillary/dataForVis/data_hierBundling')
	
