#!/usr/bin/python
# encoding: UTF-8
# mapper1.py
# Author: Ziqiang Xu
# Date: 10/11/2016
#--------------------

import sys,os,re

#pattern = re.compile(r'[A-Z]|[0-9]')

for line in sys.stdin:
    line=line.strip()
    if line:
       ll=line.split(' ')
       #ll.append(os.environ["mapreduce_map_input_file"])
       #ll.append('mapper1.txt')
       for i in ll:
          #if pattern.search(i):      
          #print("{0}\t{1}\t{2}".format(i,1,'mapper1.txt'))
          print("{0}\t{1}\t{2}".format(i,1,os.environ["mapreduce_map_input_file"]))
