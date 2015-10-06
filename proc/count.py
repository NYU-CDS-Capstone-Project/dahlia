#!/usr/bin/python

import sys

current_name = None
current_count = 0
result = []
# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
    name, count = line.strip().split("\t")
    
    try:
        count = float(count)
    except ValueError:
        continue
    
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
sorted_result = sorted(result, key=lambda x:x[1], reverse = True)[:100]
for tuple in sorted_result:
    print "%s\t%d" %( tuple[0], tuple[1])
