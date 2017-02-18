#! /bin/bash

hdfs dfs -cat /data/assignments/ex2/part3/webLarge.txt | ./bloomfilter.py > output.out
