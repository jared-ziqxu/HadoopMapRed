#! /bin/bash
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D stream.num.map.output.key.fields=2 \
-D mapreduce.partition.keypartitioner.options=-k1,1 \
-D mapreduce.partition.keycomparator.options=-k1,1 \
-input /data/assignments/ex2/part1/large/* \
-output /user/$USER/assignment2/task1 \ 
-mapper mapper1.py -file mapper1.py \ 
-combiner combiner1.py -file combiner1.py \ 
-reducer reducer1.py -file reducer1.py
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
