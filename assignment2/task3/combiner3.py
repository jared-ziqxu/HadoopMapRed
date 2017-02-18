#!/usr/bin/python

import sys,os

prev_oid = None
post_id = []

for line in sys.stdin:
    line=line.rstrip()
    ll=line.split(' ')
    if len(ll) > 1:
        oid=ll[0]
        pid=ll[1]

        if oid == prev_oid:
            post_id.append(pid)
        else:
            if prev_oid != None:
                print("{0}\t->{1}".format(prev_oid, post_id))
            prev_oid = oid
            post_id = []
            post_id.append(pid)

if oid == prev_oid:
    print("{0}\t->{1}".format(prev_oid, post_id))
        
