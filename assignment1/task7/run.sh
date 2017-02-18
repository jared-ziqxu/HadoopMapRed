#! /bin/bash
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D stream.num.map.output.key.fields=2 \
-D mapreduce.partition.keypartitioner.options=-k2,2 \
-D mapreduce.partition.keycomparator.options="-k2,2n -k1,1r" \
-input /data/assignments/ex1/uniLarge.txt \
-output /user/$USER/assignment1/task7 \
-mapper mapper7.py \
-file mapper7.py \
-reducer reducer7.py \ 
-file reducer7.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
