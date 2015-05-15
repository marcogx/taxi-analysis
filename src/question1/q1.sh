#!/usr/bin/env sh

rm -rf output/q1j1
rm -rf output/q1j2

$HADOOP_HOME/bin/hadoop  jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-1.0.3.jar \
	-D mapred.reduce.tasks=2 \
    -input input/trip_date_test \
    -output output/q1j1 \
    -mapper q1map.py \
    -reducer q1rd.py

$HADOOP_HOME/bin/hadoop  jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-1.0.3.jar \
	-D mapred.reduce.tasks=2 \
    -input output/q1j1/part* \
    -output output/q1j2/ \
    -mapper q1map2.py \
    -reducer q1rd2.py
