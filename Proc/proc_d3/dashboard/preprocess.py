import json
import sys
import string
import collections
import numpy as np
from operator import *
import itertools
import pickle
from readTweet import *
import reverse_geocoder as rg

# Retrive the top three hashtags from the preprocessed raw data
num_hash = 5

hash_top = sortLine(num_hash, 'result_hash.txt')

listStates=['Alabama', 'Alaska','Arizona','Arkansas','California','Colorado', 'Connecticut', 'Delaware', 'District of Columbia',
           'Florida','Georgia','Hawaii', 'Idaho', 'Illinois','Indiana', 'Iowa', 'Kansas','Kentucky','Louisiana','Maine','Maryland',
           'Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey',
           'New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island',
           'South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin',
           'Wyoming']

def findLocation(hashtag, coordinates):
	print 'Finding corresponding locations...'
	results_ = rg.search(coordinates)
	results = [i['admin1'] for i in results_]
	total_result = []
	for i in zip(results, hashtag):
		if len(i[1]) != 0:
			temp = []
			for j in i[1]:
				temp.append(j['text'])
			total_result.append((i[0], temp))
		else:
			total_result.append((i[0],i[1]))

	placeFinal = [i for i in total_result if i[0] in listStates]
	print 'Done'
	return placeFinal

def makeData(placeFinal):
	print 'Dumping data into json...'
	
	# a list of tag1,tag2,tag3..... of how many the user defines
	tag_total = []
	for i in range(len(hash_top)):
		tag_total.append(hash_top[i][0])

	# taglist_total = [tag_1,tag_2,tag_3,tag_4,tag_5]
	taglist_total = [[] for i in range(len(tag_total))]

	for i in placeFinal:
		for j in range(len(tag_total)):
			if tag_total[j] in i[1]:
				taglist_total[j].append(i[0])

	# collection of all the counters, aka cnt1,cnt2,cnt3....
	cnt_total = [collections.Counter(i) for i in taglist_total]
	
	# common set of states that appear in all list
	community = set.intersection(*[set(i.keys()) for i in cnt_total])

	data = []
	for i in community:
		frequency = {tag_total[j]:int(cnt_total[j][i]) for j in range(len(tag_total))}
		data.append({'State':i, 'freq': frequency})
	data_new = sorted(data, key=lambda x: sum(x['freq'].values()), reverse=True)[:8]
	json.dump(data_new, open('dashboard_data.json','wb'))
	print 'Done'

if __name__ == '__main__':
	
	hashtag = pickle.load(open('hashtag.pkl','rb'))
	coordinates = pickle.load(open('coordinates.pkl','rb'))

	placeFinal = findLocation(hashtag, coordinates)
	makeData(placeFinal)
