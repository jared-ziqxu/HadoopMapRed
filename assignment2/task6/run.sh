#! /bin/bash

hdfs dfs -cat /data/assignments/ex2/part3/webLarge.txt | ./uniSampleKline.py 2
#hdfs dfs -cat /data/assignments/ex2/part3/webLarge.txt | ./uniSampleKline.py 3
