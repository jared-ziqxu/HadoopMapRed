#!/usr/bin/python

import sys,os

prev_word = None
word = None
prev_fn = None
fn = None
freq_info = {}

for line in sys.stdin:
    line=line.rstrip()
    ll=line.split('\t')
    if len(ll) > 1:
            word=ll[0]
            value=int(ll[2])
            fn = os.path.basename(ll[1])            

    if word == prev_word:
         freq_info[fn]=value
    else:
         if prev_word != None:
             print("{0}:{1}:{2}".format(prev_word, len(freq_info),freq_info))
         freq_info = {}
         prev_word = word
         freq_info[fn]=value
       
#if prev_word == word: 
print("{0}:{1}:{2}".format(word, len(freq_info),freq_info))
        
