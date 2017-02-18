#!/usr/bin/python

import sys

prev_line = None
value_total = 0
line = None

for line in sys.stdin:
    line=line.rstrip()
    ll=line.split('\t')
    if len(ll) == 2:
            line=ll[0]
            value=int(ll[1])
    
    if line == prev_line:
        value_total = value_total + value
    else:
        if prev_line != None:
            print("{0}\t{1}".format(prev_line, value_total))
        if line and value:
            value_total = value
            prev_line = line

if prev_line == line:
    print("{0}\t{1}".format(prev_line, value_total))
