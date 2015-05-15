rm -rf output/q4
$HADOOP_HOME/bin/hadoop  jar $HADOOP_HOME/contrib/streaming/hadoop-streaming-1.0.3.jar \
    -input inputtest/trip_fare_1.csv \
    -output output/q4/ \
    -mapper q4map.py \
    -reducer q4rd.py

