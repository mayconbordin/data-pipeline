#!/bin/sh

# Wait for the Hadoop Datanode docker to be running
while ! nc -z hadoop-datanode 9864; do
  >&2 echo "Datanode is unavailable - sleeping"
  sleep 3
done

# urls="
# https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv
# https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-02.csv
# https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-03.csv
# https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-04.csv
# https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-05.csv
# https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-06.csv
# https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-07.csv
# ";

# cd /tmp && mkdir tripdata && cd tripdata || exit;
# for url in ${urls}; do wget "${url}"; done;

# hdfs dfs -mkdir -p hdfs://hadoop-namenode:8020/data/raw
# hdfs dfs -put /tmp/tripdata hdfs://hadoop-namenode:8020/data/raw

exit 0;
