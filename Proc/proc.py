import json
import gzip
import tarfile
import zipfile
import shlex
import subprocess
import sys
import string
import nltk
import goose
from pprint import pprint
from collections import Counter
import numpy as np
import os

def select_field(jsonLine):
    l = json.loads(jsonLine)
    time = str(l['created_at'])
    hashtag = str(l['entities']['hashtags'][0]['text'])
    loca = str(l['user']['location'])
    coord = str(l['coordinates']['coordinates'])
    mention = l['entities']['user_mentions'][0]['screen_name']
    source_ = l['source'].encode('ascii', 'ignore')
    source = re.sub('<[^<]+?>', '', source_)
    tweet = str(l['retweeted_status']['text'])
    person = str(l['user']['screen_name'])
    return [time, hashtag, loca, coord, mention, source, tweet, person]

def load_data(path):
    '''
    Loads the dataset
    '''

    print 'Loading data'
    if not os.path.isfile(path):
        raise ValueError("The path provided doesn't exist")
    data_dir, data_file = os.path.split(path)
    #Detect file type
    cmd = shlex.split('file --mime-type {0}'.format(path))
    result = subprocess.check_output(cmd)
    mime_type = result.split()[-1]
    dest,_ = os.path.splitext(path)
    if mime_type == 'application/x-tar':#if tar file
        t = tarfile.open(path, 'r')
        t.extractall(data_dir)
        flist = os.listdir(dest)
    elif mime_type == 'application/zip': #if zip file
        with zipfile.ZipFile(path) as zf:
            zf.extractall(data_dir)
        flist = os.listdir(dest)
    else:
        raise ValueError("Dataset must be .zip or .tar")

    Data = []
    flist = [i for i in flist if i[0]!= '.']
    ct = 0
    print 'progress: loading data...'
    for f in flist:
        try:
            data = dest + '/' + f
            with gzip.open(data, 'rb') as infile:
                for l in infile.readlines():
                    try:
                        fields = select_field(l)
                        Data.append(fields)
                    except:
                        pass
            ct += 1
            update_progress(ct/float(len(flist)))
        except:
            raise ValueError('Error with open json.gz file')
    print "Done! Your dataset has %d of valid tweets in total"%(len(Data))
    return numpy.array(Data)

def update_progress(progress):
    barLength = 10 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()
