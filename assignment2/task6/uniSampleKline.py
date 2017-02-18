#!/usr/bin/python
# encoding: UTF-8
# mapper5.py
# Author: Ziqiang Xu
# Date: 10/11/2016
#--------------------

import random, sys

resevoir_cap=int(sys.argv[1])
resevoir = []
line_number = 0

for line in sys.stdin:
    if line_number < resevoir_cap:
       resevoir.append(line.strip())
    else:
        idx = random.randint(0, line_number)
        if idx < resevoir_cap:
            resevoir[idx] = line.strip()
    
    line_number += 1

print len(resevoir),resevoir 
