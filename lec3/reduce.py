#!/usr/bin/python
import sys
split=sys.stdin.readline().split('\t')
while split[0]!='':
    #Process the first instance of a key.
    key = split[0]
    count = int(split[1])
    while True:
        #Sum subsequent instances of the key.
        split = sys.stdin.readline().split('\t')
        if split[0] != key:
            break
        count += int(split[1])
    print(key + "\t" + str(count))
