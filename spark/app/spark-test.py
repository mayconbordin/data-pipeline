from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("trip-preprocess").getOrCreate()

hdfs_namenode = "hadoop-namenode:8020"

trips_df = spark.read.csv(f"hdfs://{hdfs_namenode}/data/raw/tripdata/", header=True, inferSchema=True)

trips_df.show()



# create table mypoints (id serial, name varchar, geom geometry(Point, 4326));

# INSERT INTO mypoints(id, name, geom) VALUES(1, 'test', ST_GeomFromText('POINT(-71.060316 48.432044)', 4326));