# -*- coding: utf-8 -*-
import json
import nltk
import string
import collections
import itertools
import re
import random
from proc import *

# data = load_data('/Users/yitongwang/Desktop/NYU/DS-GA-1006/hillary/dahlia/hillary.tar')

def sunburst(data):

	exclude = set(string.punctuation)
	tweets = [i[6] for i in data]
	# Processed text (deprived of punctuations)
	text = []
	# with open('retweetText', 'rb') as f:
	for line in tweets:
	    if line != 'null':
			content = line.decode('utf-8')
			content = re.sub(r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))', '', content)
			s = ''.join(ch for ch in content if ch not in exclude)
			text.append(nltk.word_tokenize(s.strip('\n').strip('\u')))

	
	top_50 = collections.Counter(itertools.chain(*text)).most_common(50)
	top_50_words = [i[0] for i in top_50]
	start = [i[0] for i in text if len(i) != 0]
	cnt_start = dict(collections.Counter(start).most_common(10))
	second = [i[1] for i in text if len(i) > 1]
	cnt_second = dict(collections.Counter(second).most_common(40))
	third = [i[2] for i in text if len(i) > 2]
	cnt_third = dict(collections.Counter(third).most_common(40))

	fourth = [i[3] for i in text if len(i) > 3]
	cnt_fourth = dict(collections.Counter(fourth).most_common(40))

	fifth = [i[4] for i in text if len(i) > 4]
	cnt_fifth = dict(collections.Counter(fifth).most_common(40))

	sixth = [i[5] for i in text if len(i) > 5]
	cnt_sixth = dict(collections.Counter(sixth).most_common(40))

	preliminary = [i for i in text if len(i) > 5 and i[0] in cnt_start.keys() and i[1] in cnt_second.keys() and i[2] in 
	              cnt_third.keys() and i[4] in cnt_fourth.keys() and i[5] in cnt_fifth.keys()]

	all_words = collections.Counter(list(itertools.chain(*preliminary))).most_common(50)

	tweet_words = list(itertools.chain(*preliminary))

	# top 20 vocabulary
	color_profile = {}
	color = ['3182bd','6baed6','9ecae1','c6dbef','e6550d','fd8d3c','fdae6b','fdd0a2','31a354','74c476','a1d99b',
	        'c7e9c0','756bb1','9e9ac8','bcbddc','dadaeb','636363','969696','bdbdbd','d9d9d9']
	for i in set(all_words):
		color_profile[i[0]] = random.choice(color)
	json.dump(color_profile,open('color_profile.json','wb')) 

	# preliminary_final = ['-'.join(i) for i in temp]
	# preliminary_final = ['-'.join(i[:min((len(i)-1),10)]) for i in preliminary]
	preliminary_final = []
	for i in preliminary:
		element = '-'.join(i[:min(len(i)-1,10)])
		if len(i) < 10:
			element = element + str('-end')
		preliminary_final.append(element)

	with open('tweet_text.csv','wb') as f:
		for key,value in collections.Counter(preliminary_final).iteritems():
			if value > 10:
				f.write('%s,%d\n' % (key.encode('ascii', 'ignore'),value))
