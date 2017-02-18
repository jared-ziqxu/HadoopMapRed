#! /bin/bash
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -input /user/$USER/assignment1/task1/* -output /user/$USER/assignment1/task2/ -mapper mapper2.py -file mapper2.py -reducer reducer2.py -file reducer2.py


