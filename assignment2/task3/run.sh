#! /bin/bash
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \ 
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapreduce.job.reduces=1 \
-D stream.num.map.output.key.fields=1 \
-D stream.map.output.field.separator="\t" \ 
-D mapreduce.partition.keypartitioner.options=-k1,2 \
-D mapreduce.partition.keycomparator.options="-k1,1nr" \ 
-input /data/assignments/ex2/part2/stackLarge.txt \
-output /user/$USER/assignment2/task3/ \
-mapper mapper3.py -file mapper3.py \ 
-combiner combiner3.py -file combiner3.py \ 
-reducer reducer3.py -file reducer3.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
