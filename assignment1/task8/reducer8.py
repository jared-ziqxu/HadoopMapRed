#!/usr/bin/python

import sys,math


name=""
max_mark=0
    
for line in sys.stdin:
     line=line.rstrip()
     ll=line.split('\t')
     if len(ll) == 2:
          mark=ll[1]
          if int(mark)>max_mark:
             max_mark=int(mark)
             name=ll[0]

print name,max_mark 
