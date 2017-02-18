#! /bin/bash
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.reduces=1
-input /user/$USER/assignment1/task4/* \
-output /user/$USER/assignment1/task5/ \
-mapper cat \
-reducer reducer5.py \
-file reducer5.py

