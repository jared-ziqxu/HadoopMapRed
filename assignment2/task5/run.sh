#! /bin/bash

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.reduces=1 \ 
-input /data/assignments/ex2/part3/webLarge.txt \ 
-output /user/$USER/assignment2/task5 \
-mapper mapper5.py -file mapper5.py \
-reducer reducer5.py -file reducer5.py
