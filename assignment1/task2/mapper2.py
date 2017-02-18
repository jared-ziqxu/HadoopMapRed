#!/usr/bin/python

import sys

for line in sys.stdin:                  # input from standard input
    line = line.strip()                 # remove whitespaces
    print("{0}\t{1}".format(line, 1))
