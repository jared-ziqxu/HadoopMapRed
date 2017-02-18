#! /bin/bash
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -D mapreduce.job.reduces=1 -input /user/$USER/assignment1/task7/* -output /user/$USER/assignment1/task8/ -mapper mapper8.py -file mapper8.py -reducer reducer8.py -file reducer8.py
