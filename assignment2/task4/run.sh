#! /bin/bash
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \ 
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapreduce.job.reduces=1 \
-D stream.num.map.output.key.fields=3 \
-D stream.map.output.field.separator="\t" \
-D mapreduce.partition.keypartitioner.options=-k1,2 \
-D mapreduce.partition.keycomparator.options="-k2,2n -k1,1n" \
-input /data/assignments/ex2/part2/stackLarge.txt \
-output /user/$USER/output \
-mapper mapper41.py -file mapper41.py \
-reducer reducer41.py -file reducer41.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar \ 
-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
-D mapreduce.job.reduces=1 \
-D stream.num.map.output.key.fields=1 \
-D stream.map.output.field.separator=" " \
-D mapreduce.partition.keypartitioner.options=-k1 \
-D mapreduce.partition.keycomparator.options=-k1,1n \
-input /user/$USER/output \
-output /user/$USER/assignment2/task4 \
-mapper cat \
-reducer reducer42.py -file reducer42.py \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
