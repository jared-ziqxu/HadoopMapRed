#!/usr/bin/python
# encoding: UTF-8
# mapper5.py
# Author: Ziqiang Xu
# Date: 10/11/2016
#--------------------

import random, sys

line_number = 0

for line in sys.stdin:
    if random.randint(0, line_number) == 0:
        resevoir = line.strip()
    line_number += 1

print(resevoir) 
