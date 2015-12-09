import json
import itertools
import gzip
import tarfile
import zipfile
import shlex
import subprocess
import sys
import string
from nltk.corpus import stopwords
from collections import Counter
import os
import re
import reverse_geocoder as rg

def select_field(jsonLine):
    l = json.loads(jsonLine)
    time = str(l['created_at'])
    try:
        hashtag = l['entities']['hashtags']
        hashtag = [i['text'] for i in hashtag]
    except:
        hashtag = 'null'
    try:
        loca = str(l['user']['location'])
    except:
        loca = 'null'
    try:
        coord = tuple(l['coordinates']['coordinates'])[::-1]
    except:
        coord = 'null'
    try:
        mention = [i['screen_name'] for i in l['entities']['user_mentions']]
    except:
        mention = 'null'
    try:
        source = l['source']
        source = re.sub('<[^<]+?>', '', source)
    except:
        source = 'null'
    try:
        tweet = str(l['retweeted_status']['text'])
    except:
        tweet = 'null'
    try:
        person = str(l['user']['screen_name'])
    except:
        person = 'null'
    try:
        statsCount = int(l['user']['statuses_count'])
    except:
        statsCount = 'null'

    return [time, hashtag, loca, coord, mention, source, tweet, person, statsCount]

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
            update_progress(float("{0:.4f}".format(ct/float(len(flist)))))
        except:
            raise ValueError('Error with open json.gz file')
    print "Done! Your dataset has %d valid tweets in total"%(len(Data))
    return Data

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

def count_single_field(field, data):
    if field == 'hashtag':
        out = [i[1] for i in data if i[1] != 'null']
        out = Counter(list(itertools.chain.from_iterable(out)))
    if field == 'coordinates':
        coord = [i[3] for i in data if i[3] != 'null']
        result = rg.search(coord)
        out = Counter([i['admin1'] for i in result])
    if field == 'mention':
        out = Counter([i[4] for i in data if i[4] != 'null'])
    if field == 'source':
        out = Counter([i[5] for i in data if i[5] != 'null'])
    if field == 'tweet':
        out = Counter([i[6] for i in data if i[6] != 'null'])
    if field == 'user':
        out = Counter([i[7] for i in data if i[7] != 'null'])
    return out

def count_word(tweet_count, stopwords):
    exclude = string.punctuation
    stopsEng = list(stopwords.words("english"))
    stopsEsp = list(stopwords.words("spanish"))
    stops = stopsEng + stopsEsp
    count = dict()
    for k,v in tweet_count.items():
        k = k.strip()
        text = ''.join([i for i in k if i not in exclude]).lower()
        text = text.split()
        text = Counter([w for w in text if w not in stops])
        for key, val in text.items():
            if count.has_key(key):
                count[key] += val * v
            else:
                count[key] = val * v
    return count

def dict_to_dsv(dic, outfile, d = ','):
    with open(outfile, 'w') as f:
        f.write('word%scount\n'%(d))
        for k,v in dic.items():
            k = k.encode('utf-8')
            if k != '':
                f.write('%s%s%d\n'%(k,d,v))




