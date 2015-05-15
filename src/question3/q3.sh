#!/usr/bin/env bash

# clean up output folder
# rm -rf output/q3

# test code
# cat inputtest/trip_data_test_1 | python q3map.py| sort |python q3rd.py

# hadoop streamming job
$HADOOP_HOME/bin/hadoop  jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-1.0.3.jar \
    -input input/trip_data* \
    -output output/q3j1/ \
    -mapper q3map.py \
    -reducer q3rd.py
