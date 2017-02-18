#!/usr/bin/python

import sys


for line in sys.stdin:
    line=line.rstrip()
    ll=line.split()
    #if len(ll) == 4:
    #  print("{}\t{}\t{}\t{}".format(ll[0],ll[1],ll[2],ll[3])
    if len(ll) == 4:
       print("{}\t{}\t{}\t{}".format(ll[0],ll[1],ll[2],ll[3]))
 
    if len(ll) == 3:
       print("{}\t{}\t{}".format(ll[0],ll[1],ll[2])) 
