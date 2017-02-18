#! /bin/bash

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -input /user/$USER/assignment1/task2/* -output /user/$USER/assignment1/task4/ -mapper mapper4.py -file mapper4.py -reducer reducer4.py -file reducer4.py
