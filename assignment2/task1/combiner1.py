#!/usr/bin/python

import sys,os

prev_word = None
value_total = 0
word = None
prev_fn = None
fn = None

for line in sys.stdin:
    line=line.rstrip()
    ll=line.split('\t')
    if len(ll) > 1:
            word=ll[0]
            value=int(ll[1])
            fn = os.path.basename(ll[2])            

    if word == prev_word:
        if fn == prev_fn: 
          value_total = value_total + value
        else:
          print("{0}\t{2}\t{1}".format(prev_word, value_total, fn))
    else:
        if prev_word != None:
            print("{0}\t{2}\t{1}".format(prev_word, value_total, fn))
        if word and value and fn:
            value_total = value
            prev_word = word
            prev_fn = fn
            
#if prev_word == word: 
print("{0}\t{2}\t{1}".format(word, value_total,fn))
        
