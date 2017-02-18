#! /bin/bash
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -input /data/assignments/ex1/webLarge.txt -output /user/$USER/assignment1/task1 -mapper cat -reducer reducer1.py -file reducer1.py
