import os
from pyspark.sql import SparkSession

# PATH_TO_JAR_FILE = "/opt/postgresql-42.3.5.jar"
# spark = SparkSession \
#     .builder \
#     .appName("Example") \
#     .config("spark.jars", PATH_TO_JAR_FILE) \
#     .getOrCreate()
spark = SparkSession \
    .builder \
    .appName("Example") \
    .getOrCreate()

hdfs_namenode = "hadoop-namenode:8020"

preprocess_data = spark.read.format("parquet").load(f"hdfs://{hdfs_namenode}/data/trusted/tripdata/")

preprocess_data.write \
    .format("jdbc") \
    .mode("append") \
    .option("url", f"jdbc:postgresql://analytics-postgres:5432/analytics") \
    .option("user", "analytics") \
    .option("password", "analytics") \
    .option("driver", "org.postgresql.Driver") \
    .option("dbtable", "staging_tripdata") \
    .save()

print("done")
# df.write.jdbc(url=f"jdbc:postgresql://analytics-postgres:5432/analytics", table="staging_tripdata", mode="append", properties=properties)


# df = spark.read \
#     .format("jdbc") \
#     .option("url", f"jdbc:postgresql://analytics-postgres:5432/analytics") \
#     .option("user", "analytics") \
#     .option("password", "analytics") \
#     .option("driver", "org.postgresql.Driver") \
#     .option("query","select * from links") \
#     .option('fetchsize',"1000") \
#     .load()

# df.printSchema()
# df.show()
# import os
# from pyspark.sql import SparkSession

# PATH_TO_JAR_FILE = "/home/jovyan/postgresql-42.3.5.jar"
# spark = SparkSession \
#     .builder \
#     .appName("Example") \
#     .config("spark.jars", PATH_TO_JAR_FILE) \
#     .getOrCreate()

# DB_HOST = os.environ.get("PG_HOST")
# DB_PORT = os.environ.get("PG_PORT")
# DB_NAME = os.environ.get("PG_DB_CLEAN")
# DB_PASSWORD = os.environ.get("PG_PASSWORD")
# DB_USER = os.environ.get("PG_USERNAME")

# df = spark.read \
#     .format("jdbc") \
#     .option("url", f"jdbc:postgresql://{DB_HOST}:{DB_PORT}/{DB_NAME}") \
#     .option("user", DB_USER) \
#     .option("password", DB_PASSWORD) \
#     .option("driver", "org.postgresql.Driver") \
#     .option("query","select * from your_table") \
#     .option('fetchsize',"1000") \
#     .load()

# df.printSchema()