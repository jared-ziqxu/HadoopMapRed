#!/usr/bin/python

import sys,operator

top_20={}


for line in sys.stdin:
    line=line.rstrip()
    ll=line.split('\t')
    if len(ll) == 2:
        line=ll[0]
        value=int(ll[1])
        
        if len(top_20)<20:
            #not enough 20 item, add in
            top_20[line]=value
        else:
            min_top20 = min(top_20.itervalues())
            if value > min_top20:
                #remove the smallest in top 20
                kk=[k for k, v in top_20.iteritems() if v == min_top20]
                if len(kk) > 0:
                    #if several found, just pop out the first
                    top_20.pop(kk[0])
                    #add the current line into top 20
                    top_20[line]=value


for k,v in sorted(top_20.items(), key=operator.itemgetter(1), reverse=True): 
    print("{0}\t{1}".format(k, v)) 
    
     
        
 
