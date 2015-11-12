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
hash_top = sortLine(10, 'result_hash.txt')
tag1, tag2, tag3 = hash_top[0][0], hash_top[1][0], hash_top[2][0]
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
	tag_1 = []
	tag_2 = []
	tag_3 = []
	for i in placeFinal:
		if tag1 in i[1]:
			tag_1.append(i[0])
		if tag2 in i[1]:
			tag_2.append(i[0])
		if tag3 in i[1]:
			tag_3.append(i[0])
	cnt1 = collections.Counter(tag_1)
	cnt2 = collections.Counter(tag_2)
	cnt3 = collections.Counter(tag_3)

	community = set(tag_1) ^ set(tag_2) ^ set(tag_3)

	data = []
	for i in community:
		data.append({'State': i, 'freq':{tag1: int(cnt1[i]), tag2: int(cnt2[i]), tag3:int(cnt3[i])}})

	data_new = sorted(data, key=lambda x: sum(x['freq'].values()), reverse=True)[:8]
	json.dump(data_new, open('dashboard_data.json','wb'))
	print 'Done'

if __name__ == '__main__':
	hashtag = pickle.load(open('hashtag.pkl','rb'))
	coordinates = pickle.load(open('coordinates.pkl','rb'))

	placeFinal = findLocation(hashtag, coordinates)
	makeData(placeFinal)
