#!/usr/bin/python

import sys
import re
current_name = None
current_count = 0
result = []
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    try:
        name, count = line.strip().split("\t")
    except:
        name = line.strip()
        count = 1
    
    try:
        count = float(count)
    except ValueError:
        continue
    name = re.sub('<[^<]+?>', '', name)
    if name == current_name:
        current_count += count
    else:
        if current_name:
            tu = (current_name, current_count)
            result.append(tu)
        current_name = name
        current_count = count
        
# output goes to STDOUT (stream data that the program writes)
tu = (current_name, current_count)
result.append(tu)
sorted_result = sorted(result, key=lambda x:x[1], reverse = True)
for tuple in sorted_result:
    print "%s\t%d" %( tuple[0], tuple[1])
