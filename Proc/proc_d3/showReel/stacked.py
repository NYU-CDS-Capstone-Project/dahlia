import json
import pickle
import itertools
import collections
import operator
import datetime
from proc import *

top = 6
month_correspondance={'Jan':1,'Feb':2,'Mar':3,"Apr":4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}

def stacked(data,top):
    data_ = [(i[0],i[1]) for i in data if len(i[1]) > 0]
    hashtag = list(itertools.chain(*[i[1] for i in data_]))
    tophash = dict(collections.Counter(hashtag).most_common(top))
    
    # data_new only contains data where the top n most common hashtags appear
    data_new = [i for i in data_ if len(set(i[1]).intersection(set(tophash.keys()))) > 0]
    
    # data_final:list of tuples where each tuple is a flattened out from data_new and iff i[1] in top4hash.keys()
    # eliminate out elements in data_new where some hashtags in data_new are not from the top 4
    data_final = list(itertools.chain(*[[(i[0],j) for j in i[1] if j in tophash.keys()] for i in data_new]))
    
    temp = []
    for i in tophash.keys():
        temp.append([j for j in data_final if j[1] == i])
        
    category = []
    epoch = datetime.datetime.utcfromtimestamp(0)
    for i in temp:
        wtf = []
        for j in i:
            time = j[0].split(' ')
            month,day,hour,year = month_correspondance[time[1].encode('ascii','ignore')],time[2].encode('ascii','ignore'),time[3].encode('ascii','ignore').split(':')[0],time[-1].encode('ascii','ignore')
            # wtf.append(('%s%s-%s-%s' % (month,day,year,hour),j[1]))
            wtf.append((((datetime.datetime(int(year),int(month),int(day),int(hour)) - epoch).total_seconds() * 1000.0),j[1]))
        category.append(wtf) 
    
    data_FINAL = []
    timecnt = []
    for i in category:
        sort_list = sorted(i,key=lambda x: (x[0]))
        all_time = set([x[0] for x in sort_list])
        timecnt.append(all_time)
        data_FINAL.append(sort_list)
        
        
    data_final_total = []
    for i in data_FINAL:
        cnt = collections.Counter(i)
        item = {}
        item["key"] = i[1][1]
        temp = []
        for key,value in cnt.iteritems():
            temp.append([int(key[0]),float(value)])
        item["values"] = sorted(temp, key=lambda x: x[0])
        data_final_total.append(collections.OrderedDict(sorted(item.items())))
    
    with open('data_tweet.json','wb') as f:
        json.dump(data_final_total,f)

# if __name__ == '__main__':
#     data = load_data('/Users/yitongwang/Desktop/NYU/DS-GA-1006/hillary/dahlia/hillary.tar')
#     # top: number of entities that one wants to compare
#     make_data(data,top)
