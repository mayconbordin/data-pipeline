
# data-pipeline

This is a local data pipeline that uses Airflow for orchestration, Spark for data processing, HDFS for raw data storage and PostgreSQL for analytical data storage.

This pipeline has an Airflow DAG that listens to files on HDFS. When a file arrives in HDFS the processing starts, with Spark processing data, storing on HDFS and then moving the data to PostgreSQL. Within PostgreSQL the data is stored in a staging table and with Airflow we move the data to another table, parsing the coordinate columns into PostGIS type columns.

In the end, we have a Flask API exposing the data from PostgreSQL.

## Quick Start

1. Clone the repository

2. Install [Docker](https://docs.docker.com/engine/install/)

3. Run the following command to start the infrastructure:

```
cd data-pipeline
docker-compose up
```

4. Open Airflow at http://localhost:8080/ (user = admin, password = admin), go to DAG tripdata-process and click on Trigger DAG

5. Run the following command to copy the CSV file to HDFS:

```bash
make add-file
```

6. Wait for the DAG sensor to find out the file and finish execution.

7. Connect to PostgreSQL:

```sql
docker exec -it analytics-postgres bash
psql --username=analytics
\c analytics
select * from staging_tripdata limit 10;
select * from tripdata limit 10;
```

8. Get the weekly average within a bounding box from the API:

```
wget http://localhost:50555/
```

## Infrastructure on AWS

![Infrastructure on AWS](/img/aws-infra.png)

This is the proposed infrastructure on AWS. Airflow would be deployed on ECS, the storage would be S3, the database would be an RDS, Redis would be ElastiCache Redis and the Spark Cluster would be with EMR.

We could also leverage S3 notifications to send and SNS event every time a file is uploaded to S3, and then use this event to trigger the DAG. And we can also create and destroy EMR clusters on the DAG, to avoid having a Spark cluster always on.


## Improvements

 - Incremental loads: for simplicity, I'm loading all data at every execution, but some simple changes like removing the processed files, could be implemented to avoid processing all data everytime. Likewise, on PostgreSQL we could use a timestamp column to control which data was already loaded.