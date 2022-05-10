ARG AIRFLOW_BASE_IMAGE="apache/airflow:2.2.5-python3.8"
FROM ${AIRFLOW_BASE_IMAGE}

USER root

RUN apt update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Setup JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
RUN export JAVA_HOME

RUN curl https://jdbc.postgresql.org/download/postgresql-42.3.5.jar --output /opt/postgresql-42.3.5.jar
RUN chown airflow /opt/postgresql-42.3.5.jar

USER airflow

RUN pip install --user --no-cache-dir \
    minio==5.0.10 \
    apache-airflow-providers-amazon==3.3.0 \
    pyspark==3.2.1 \
    apache-airflow-providers-apache-spark==2.1.3 \
    apache-airflow-providers-apache-hdfs==2.1.1 \
    apache-airflow-providers-postgres==4.1.0 \
    hdfs==2.7.0;
