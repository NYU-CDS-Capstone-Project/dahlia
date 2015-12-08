#!/usr/bin/env python

import sys
import string
import os
import cPickle
import reverse_geocoder as rg
from collections import Counter
def mapCoor(coo):
    results_ = rg.search(coo)
    c = Counter([i['admin1'] for i in results_])
    return c

def dict2csv(dic, outfile):
    f = open(outfile, 'w')
    f.write('word,count\n')
    for k,v in dic.items():
        f.write('%s,%d\n'%(k,v))
    f.close()

if __name__ =='__main__':
    c = cPickle.load(open('../dashboard/coordinates.pkl','rb'))
    c = mapCoor(c)
    dict2csv(c, '../../../Vis/data/')
    

