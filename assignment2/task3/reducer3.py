#!/usr/bin/python

import sys,os

max_pid=[]
max_oid=0
max_pid_sum=0
for line in sys.stdin:
    line=line.rstrip()
    ll=line.split('\t')
    if len(ll) > 1:
        oid=ll[0]
        pid=ll[1]
        pid_sum = len(pid.split(',')) 
        if pid_sum > max_pid_sum:
          max_pid = pid
          max_oid = oid
          max_pid_sum = pid_sum

print max_oid,max_pid 
