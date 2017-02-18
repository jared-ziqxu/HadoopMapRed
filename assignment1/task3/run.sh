#! /bin/bash

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -input /user/$USER/assignment1/task2/* -D mapreduce.job.reduces=1 -output /user/$USER/assignment1/task3/ -mapper mapper3.py -file mapper3.py -reducer reducer3.py -file reducer3.py

