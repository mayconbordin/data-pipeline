from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("preprocess")\
                .getOrCreate()

hdfs_namenode = "hadoop-namenode:8020"

trips_df = spark.read.csv(f"hdfs://{hdfs_namenode}/data/raw/tripdata/", header=True, inferSchema=True)

preprocess_data = trips_df \
                    .withColumn("datetime", to_timestamp("datetime", "yyyy-MM-dd HH:mm:ss"))

preprocess_data.write \
    .format("parquet") \
    .mode("append") \
    .save(f"hdfs://{hdfs_namenode}/data/trusted/tripdata/")
