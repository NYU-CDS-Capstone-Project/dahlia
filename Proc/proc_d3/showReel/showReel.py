import json
import pickle
import itertools
import collections
import operator
import datetime
from proc import *

def showReel(data):

    month_correspondance={'Jan':1,'Feb':2,'Mar':3,"Apr":4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
    # data = load_data('/Users/yitongwang/Desktop/NYU/DS-GA-1006/hillary/dahlia/hillary.tar')

    data_ = [(i[0],i[1]) for i in data if len(i[1]) > 0]
    hashtag = list(itertools.chain(*[i[1] for i in data_]))
    tophash = dict(collections.Counter(hashtag).most_common(4))

    # data_new only contains data where the top n most common hashtags appear
    data_new = [i for i in data_ if len(set(i[1]).intersection(set(tophash.keys()))) > 0]
    # data_final:list of tuples where each tuple is a flattened out from data_new and iff i[1] in top4hash.keys()
    # eliminate out elements in data_new where some hashtags in data_new are not from the top 4
    data_final = list(itertools.chain(*[[(i[0],j) for j in i[1] if j in tophash.keys()] for i in data_new]))

    data_FINAL = []
    for i in data_final:
        time = i[0].split(' ')
        tag = i[1]
        month,day,year,hour = time[1],time[2],time[-1],time[3].split(':')[0]
        reformed_time = '-'.join([month,day,year,hour])
        data_FINAL.append((reformed_time, tag))

    data_FINAL_1 = []
    for key,value in collections.Counter(data_FINAL).iteritems():
        data_FINAL_1.append((key,value))

    data_FINAL_1 = sorted(data_FINAL_1, key=lambda x:(x[0][1], int(x[0][0].split('-')[1]),int(x[0][0].split('-')[-1]),month_correspondance[x[0][0].split('-')[0]],int(x[0][0].split('-')[2])))

    with open('data_tweet.csv','wb') as f:
        f.write('symbol,date,price\n')
        for i in data_FINAL_1:
            f.write('%s,%s,%d\n' % (i[0][1],i[0][0],i[1]))