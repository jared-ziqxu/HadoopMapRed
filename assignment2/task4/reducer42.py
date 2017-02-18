#!/usr/bin/python
# encoding: UTF-8
# mapper1.py
# Author: Ziqiang Xu
# Date: 10/11/2016
#--------------------

import sys,os,re

max_u_id = 0
max_u_ans = []
max_an_num = 0

user = 0

curr_uid = 0
curr_u_ans = []

for line in sys.stdin:
    line=line.strip()
    ll=line.split("\t")
    if len(ll) > 1:
      user=int(ll[0])
      ans_id = ll[1]
      #print user, u_id
      #print user == u_id 
      if user != curr_uid:
         if len(curr_u_ans) > max_an_num:
            max_u_id = curr_uid
            max_u_ans = curr_u_ans
            max_an_num = len(curr_u_ans) 
         #print '{}:{}:{}'.format(u_id,len(u_ans),u_ans)
         curr_uid = user
         curr_u_ans = []
         curr_u_ans.append(ans_id)
      else:
         curr_u_ans.append(ans_id)

print '{} -> {},{}'.format(max_u_id,max_an_num,max_u_ans)
