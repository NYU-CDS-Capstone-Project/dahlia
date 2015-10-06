#!/usr/bin/env python
import zipimport
importer = zipimport.zipimporter('nltkandnameparser.mod')
yaml = importer.load_module('nameparser')
nltk = importer.load_module('nltk') 

from nameRecognition import *
import os
import sys

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


