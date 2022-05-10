FROM jupyter/pyspark-notebook:spark-3.2.1

USER jovyan

RUN wget -O /home/jovyan/postgresql-42.3.5.jar https://jdbc.postgresql.org/download/postgresql-42.3.5.jar

RUN pip install --no-cache-dir \
    numpy==1.22.3;