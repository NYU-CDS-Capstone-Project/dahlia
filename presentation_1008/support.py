import json
import sys
import string
import nltk
import goose
from pprint import pprint
import collections
import matplotlib.pyplot as plt
import numpy as np
import shlex, subprocess
from operator import *
import xml
import re

def get_count():
    # command_line = raw_input("Please enter your command")
    command_line = 'wc -l ../*.json'
    p = subprocess.Popen(command_line, stdout = subprocess.PIPE, stderr=subprocess.PIPE, shell='True')
    stdout, stderr = p.communicate()
    return stdout

def parse_count(stdout):
    # return the count of tweet per hour in a different data structure
    parsed_out = stdout.split('\n')
    total = parsed_out[-2].strip().split(' ')[0]
    print 'Total number of tweet is : %s' % (total)
    return parsed_out[:-2]

def analyze_count(out, title):
    # Graph the count distribution
    name = []
    count = []
    for i in out:
        element = i.strip().split(' ')
        count.append(int(element[0]))
        name.append(element[1][11:16])
    x = np.array(range(len(name)))
    y = np.array(count)
    x_label = np.array(name)
    plt.figure(figsize=(20,10))
    plt.xticks(x, x_label, rotation = 90, fontsize = 18)
    plt.bar(x, y)
    plt.title(title, fontsize = 30)
    plt.show()

# Open the mapreduce output and sort the elements by their individual counts
# inp: input; top: top N you'd like to see
def sortLine(inp, top):
    lines = []
    for line in inp.readlines():
        l = line.strip('\n').split('\t')
        new = (l[:-1][0].decode('utf-8').encode('ascii', 'ignore'), int(l[-1]))
        lines.append(new)

    lines_new = sorted(lines, key = itemgetter(1), reverse = True)
    return lines_new[:top]

# Graph the count distribution of mapreduce results
def graphing(data, title):
    name, count = zip(*data)
    x = np.array(range(len(data)))
    y = np.array(count)
    x_label = np.array(name)
    plt.figure(figsize = (20,10))
    plt.xticks(x, x_label, rotation = 90)
    plt.bar(x, y)
    plt.title(title)
    plt.show()


