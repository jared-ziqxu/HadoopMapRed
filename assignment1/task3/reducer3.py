#!/usr/bin/python

import sys

max_token = 0
max_line = 0

for line in sys.stdin:
    line=line.rstrip()
    ll=line.split()
        
    if len(ll) == 2:
            token_len=ll[0]
            line_len=ll[1]
    
    if token_len and line_len:
             
             if max_token < token_len:
                  max_token = token_len
             if max_line < line_len:
                  max_line = line_len

print max_token, max_line 
