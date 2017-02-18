#!/usr/bin/python
# encoding: UTF-8
# mapper1.py
# Author: Ziqiang Xu
# Date: 10/11/2016
#--------------------

import sys,os,re

for line in sys.stdin:
    line=line.strip()
    pattern=re.compile(r'PostTypeId=\"(\d+)\"')
    res=pattern.search(line)
    
    if res and len(res.groups())>0:
      
     #Question
     if int(res.groups()[0]) == 1:
         pattern = re.compile(r'Id=\"(\d+)\".*AcceptedAnswerId=\"(\d+)\"')
         res=pattern.search(line)
         if res and len(res.groups())>1:
            print ('1\t{}\t{}'.format(res.groups()[0],res.groups()[1]))
     #Answer
     elif int(res.groups()[0]) == 2:
         pattern = re.compile(r'Id=\"(\d+)\".*ParentId=\"(\d+)\".*OwnerUserId=\"(\d+)\"')
         res=pattern.search(line)
         if res and len(res.groups())>2:
            print ('2\t{}\t{}\t{}'.format(res.groups()[1], res.groups()[0], res.groups()[2]))
     else:
         pass
