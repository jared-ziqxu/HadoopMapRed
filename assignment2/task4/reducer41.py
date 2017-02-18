#!/usr/bin/python
# encoding: UTF-8
# mapper1.py
# Author: Ziqiang Xu
# Date: 10/11/2016
#--------------------

import sys,os,re

acpt_id = 0

for line in sys.stdin:
    line=line.strip()
    ll=line.split("\t")
    if len(ll)>0: 
       if int(ll[0])==1:
           #print "111"
           #question print
           #1,q_id, acpt_id
           acpt_id = int(ll[2])
           #acpt_id = accept_ans
       elif int(ll[0])==2:
           #print "222"
           #print ll[2],acpt_id
           #answer print
           #2,q_id,ans_id,u_id
           if int(ll[2]) == acpt_id:
                #print user_id, answer_id
                print ll[3],ll[2]
       else:
           pass           
    
