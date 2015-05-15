#!/usr/bin/env bash

# clean up output folder
rm -rf output/q2

# test code
# cat inputtest/trip_fare_test_1 | python q2map.py| sort |python q2rd.py

# hadoop streaming job
$HADOOP_HOME/bin/hadoop  jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-1.0.3.jar \
    -input input/trip_fare* \
    -output output/q2/ \
    -mapper q2map.py \
    -reducer q2rd.py

