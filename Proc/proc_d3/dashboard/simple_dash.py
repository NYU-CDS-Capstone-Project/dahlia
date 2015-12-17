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
from proc import *
import itertools

def dash_board(data):
    hashtags = []
    coordinates = []
    # all hashtags
    hashtags_total = []
    for i in data:
        hashtags_total.append(i[1])
        if i[3] != 'null':
            hashtags.append(i[1])
            # now assuming: it's reversed
            # coordinates.append(i[3][::-1])
            coordinates.append(i[3])
    
    def findLocation(hashtag, coordinates):
        print 'Finding corresponding locations...'
        results_ = rg.search(coordinates)
        # print results_
        results = [i['admin1'] for i in results_]

        total_result = []
        for i in zip(results, hashtag):
            if len(i[1]) != 0:
                temp = []
                for j in i[1]:
                    temp.append(j)
                total_result.append((i[0], temp))
            else:
                total_result.append((i[0],i[1]))

        # placeFinal = [i for i in total_result if i[0] in listStates]
        placeFinal = [i for i in total_result]
        print 'Done'
        return placeFinal
    
    placeFinal = findLocation(hashtags, coordinates)
    
    def makeData(placeFinal,hash_top):
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
        # print community

        data = []
        for i in community:
            frequency = {tag_total[j]:int(cnt_total[j][i]) for j in range(len(tag_total))}
            data.append({'State':i, 'freq': frequency})
        data_new = sorted(data, key=lambda x: sum(x['freq'].values()), reverse=True)[:8]
        json.dump(data_new, open('dashboard_data.json','wb'))
        print 'Done'
        
    def sortLine(top, hashtags):
        print 'Sorting the raw results...'
        # lines = [i[1] for i in placeFinal]
        cnt_hash = [i for i in collections.Counter(itertools.chain(*[i for i in hashtags])).most_common(top)]
        return cnt_hash
    
    hashtop = sortLine(5, hashtags_total)
    
    makeData(placeFinal,hashtop)