#!/usr/bin/python

import sys


for line in sys.stdin:
    line=line.rstrip()
    print len(max(line.split(), key=len)),len(line)
    
