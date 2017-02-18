#!/usr/bin/python
# encoding: UTF-8
# mapper5.py
# Author: Ziqiang Xu
# Date: 10/11/2016
#--------------------

import numpy as np

class bitarray:

    def __init__(self,length):
       assert length>0, 'length should be greater than 0'
       self.length = length
       self.bitarray = np.zeros(length, dtype=np.int)
   
    def __str__(self):
       return np.array_str(self.bitarray)

    def __getitem__(self, i):
       assert i >= 0 and i <= self.length-1, 'out of range'
       return self.bitarray[i]
    
    def __setitem__(self,i,target):
       assert i >= 0 and i <= self.length-1, 'out of range'
       assert target == 0 or target == 1, 'only binary allowed'
       self.bitarray[i]=target
