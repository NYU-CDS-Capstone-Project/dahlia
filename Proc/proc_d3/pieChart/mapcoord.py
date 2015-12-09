#!/usr/bin/env python

import sys
import string
import os
import cPickle
import reverse_geocoder as rg
from collections import Counter

def txtCoor(infile):
    coord = []
    with open(infile,'r') as f:
        for i in f.readlines():
            l = eval(i.strip())
            if len(l) != 4:
                l = tuple(eval(l))
                coord.append(l)
    results_ = rg.search(coord)
    c = Counter([i['admin1'] for i in results_])
    return c
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
    '''
    Hillary Data

    with open('../dashboard/coordinates.pkl','rb') as f:
        count = cPickle.load(f)
    c = mapCoor(count)
    dict2csv(c, '../../../Vis/data/stateCount.csv')
    '''
    #Oscar data
    c = txtCoor('../../../Data/Oscar/result_coord.txt')
    dict2csv(c, '../../../Vis/data_o/stateCount.csv')
