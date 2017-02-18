#!/usr/bin/python
# encoding: UTF-8
# bloomfilter.py
# Author: Ziqiang Xu
# Date: 10/11/2016
#--------------------
import sys
from bitarrayfake import bitarray
from murmurhash import murmur
from math import e
from numpy.lib.scimath import logn

class bloomFilter:
    
    def __init__(self, size=0):
        #size: the number of all items
        #bit_size: the length of the bitarray 
        #hashnum: defines how many hash function used
        self.size = size
        # --------------------------------------
        # bitarray size should use this fomular
        # bit_size = -size*lnp/(ln2).^2
        # where p == 0.01 false positive percentage
        #--------------------------------------
        self.bit_size = int(-self.size*logn(e, 0.01)/(logn(e,2)**2))
        #print self.bit_size
        self.bitarray = bitarray(self.bit_size)
        #print self.bitarray
        # --------------------------------------
        # hash function number should use this fomular
        # hash function number = ln2* bitarray size/item size
        #--------------------------------------
        self.hashnum = int(logn(e,2)*self.bit_size/self.size)
        #print self.hashnum
        

    def addItem(self, word):
        #self.size += 1
        #print self.hashnum
        for hseed in xrange(self.hashnum):
            hash_raw = murmur(word, hseed)
            res = hash_raw % self.size
            #print res
            self.bitarray[res] = 1
        #self.updateParams(self.size)
        #print self.bitarray
   
    def searchItem(self, word):
        for hseed in xrange(self.hashnum):
            res = murmur(word, hseed) % self.size
            #print res
            if self.bitarray[res] == 0:
               return False
            else:
               return True
    ''' 
    def updateParams(self, size):
        # --------------------------------------
        # bitarray size should use this fomular
        # bit_size = -size*lnp/(ln2).^2
        # where p == 0.01
        #--------------------------------------
        self.bit_size = int(-self.size*logn(e, 0.01)/(logn(e,2)**2))
        self.bitarray = bitarray(self.bit_size)
        print self.bitarray
        # --------------------------------------
        # hash function number should use this fomular
        # hash function number = ln2* bitarray size/item size
        #--------------------------------------
        self.hashnum = int(logn(e,2)*self.bit_size/self.size)
    '''  
    

if __name__ == "__main__":
    #total line of webLarge.txt is 1897987
    Bfilter = bloomFilter(1897987);  
    for line in sys.stdin: 
       line=line.strip()
       if Bfilter.searchItem(line):
          continue
       else:
          Bfilter.addItem(line)
          print line
    
    #word1='hello'
    #word2='cat' 
    #line = '''9i has not BOOLEAN data CheckBoxes in are BOOLEAN controls are they using a column with Y or N values in the Oracle how do I bind to a CheckBox or CheckBoxList or RadioButton or RadioButtonList control on an web using since a an FormView CheckBox or RadioButton to Oracle''' 
    #print Bfilter.searchItem(word1)
    #print Bfilter.searchItem(word2)
    #print Bfilter.searchItem(line)

