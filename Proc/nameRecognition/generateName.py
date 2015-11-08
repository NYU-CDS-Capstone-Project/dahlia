#!/usr/bin/env python
#import zipimport
#importer = zipimport.zipimporter('nltkandnameparser.mod')
#nameparser = importer.load_module('nameparser')
#nltk = importer.load_module('nltk') 

import os
import sys
from nltk import sent_tokenize, word_tokenize, pos_tag, ne_chunk
import nltk
#from nameparser.parser import HumanName

def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)
    person_list = []
    person = []
    name = ""
    
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1: #avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []
    return (person_list)
def mapper():
    for line in sys.stdin:
        try:
            _, text = eval(line)
            text = text.decode("utf-8").encode("ascii","ignore")
            names = get_human_names(text)
            if len(names)>0:
                for i in names:
                    print "%s\t%d"%(i ,1)
            else:
                pass
        except:
            pass

if __name__=='__main__':
    mapper()

