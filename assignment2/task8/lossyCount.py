#!/usr/bin/python
# encoding: UTF-8
# lossyCount.py
# Author: Ziqiang Xu
# Date: 10/11/2016
#--------------------
import sys

item_triplets = {}
bucket_id = 1
item_count = 0 
epsilon = 0.001

for line in sys.stdin:
    line=line.strip()
    item_count += 1
    if line in item_triplets:
        #increase item frequency
        item_triplets[line][0] += 1
    else:
        #new item with frequency == 1 and delta == bucket_id-1 
        item_info = [1,bucket_id-1]
        item_triplets[line]=item_info 
    
    if item_count % int(1 / epsilon) == 0:
        for k, v in item_triplets.items():
             if v[0]+v[1] < bucket_id:
                 item_triplets.pop(k)
        bucket_id += 1

for k, v in item_triplets.items():
       #only frequency greater than 0.9% will be printed
       if v[0] > 0.009*item_count:
           print k, v[0] 
