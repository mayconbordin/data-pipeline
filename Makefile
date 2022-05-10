
add-file:
	docker cp dataset/trips.csv hadoop-namenode:/
	docker exec hadoop-namenode bash -c 'hadoop dfs -mkdir -p hdfs:///data/raw/tripdata/'
	docker exec hadoop-namenode bash -c 'hadoop fs -copyFromLocal /trips.csv hdfs:///data/raw/tripdata/trips.csv'
