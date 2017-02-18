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
    #print len(res.groups())>0
    #print res.groups()[0]==1
    
    if len(res.groups())>0 and int(res.groups()[0]) == 1:
      pattern = re.compile(r'Id=\"(\d+)\".*ViewCount=\"(\d+)\"')
      res=pattern.search(line)
      if len(res.groups())>1:
        print res.groups()[1], res.groups()[0]
