#!/usr/bin/python

import sys


for line in sys.stdin:
    new_line = " "
    line=line.rstrip()
    ll=line.split()
    for i in range(len(ll)):
       if i+3 <= len(ll):
         #new_line=new_line.join(ll[i:i+3])
         print("{0}\t{1}".format(new_line.join(ll[i:i+3]), 1))
