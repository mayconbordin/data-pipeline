from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from airflow.providers.apache.hdfs.sensors.hdfs import HdfsSensor
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta

###############################################
# Parameters
###############################################
spark_master = "spark://spark-master:7077"
spark_app_name = "Tripdata Process"

###############################################
# DAG Definition
###############################################
now = datetime.now()

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(now.year, now.month, now.day),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "is_paused_upon_creation": False,
    "retry_delay": timedelta(minutes=1)
}

dag = DAG(
        "tripdata-process", 
        default_args=default_args, 
        schedule_interval=timedelta(1)
    )

hdfs_sense_open = HdfsSensor(
    task_id='hdfs_sense_open',
    filepath='/data/raw/tripdata',
    hdfs_conn_id='hdfs_default',
    dag=dag)

spark_preprocess_job = SparkSubmitOperator(
    task_id="spark_preprocess_job",
    application="/usr/local/spark/app/spark-preprocess.py",
    name=spark_app_name,
    conn_id="spark_default",
    verbose=1,
    conf={"spark.master":spark_master},
    application_args=[],
    executor_memory="2G",
    executor_cores=1,
    num_executors=1,
    dag=dag)

spark_postgres_job = SparkSubmitOperator(
    task_id="spark_postgres_job",
    application="/usr/local/spark/app/spark-postgres.py",
    name=spark_app_name,
    conn_id="spark_default",
    verbose=1,
    conf={"spark.master":spark_master},
    jars="/opt/postgresql-42.3.5.jar",
    application_args=[],
    executor_memory="2G",
    executor_cores=1,
    num_executors=1,
    dag=dag)

create_trip_table = PostgresOperator(
    task_id="create_trip_table",
    postgres_conn_id="postgres_default",
    sql="sql/tripdata_schema.sql",
    dag=dag
)

load_trip_table = PostgresOperator(
    task_id="load_trip_table",
    postgres_conn_id="postgres_default",
    sql="INSERT INTO tripdata SELECT region, ST_GeomFromText(origin_coord, 4326), ST_GeomFromText(destination_coord, 4326), datetime, datasource FROM staging_tripdata;",
    dag=dag
)

hdfs_sense_open >> spark_preprocess_job >> spark_postgres_job >> create_trip_table >> load_trip_table
