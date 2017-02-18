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
    
    if len(res.groups())>0 and int(res.groups()[0]) == 2:
      pattern = re.compile(r'Id=\"(\d+)\".*OwnerUserId=\"(\d+)\"')
      res=pattern.search(line)
      if len(res.groups())>1:
        print res.groups()[1], res.groups()[0]
