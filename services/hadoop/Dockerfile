FROM openjdk:8
RUN apt-get update
#RUN apt-get install -y default-jdk wget
RUN apt-get install -y wget netcat-openbsd
RUN wget https://archive.apache.org/dist/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz
RUN tar xvzf hadoop-3.2.1.tar.gz && mkdir -p /usr/local/hadoop && mv hadoop-3.2.1/* /usr/local/hadoop && rm -rf hadoop-3.2.1
ENV HADOOP_INSTALL=/usr/local/hadoop
ENV PATH=$PATH:$HADOOP_INSTALL/bin
ENV PATH=$PATH:$HADOOP_INSTALL/sbin
ENV HADOOP_MAPRED_HOME=$HADOOP_INSTALL
ENV HADOOP_COMMON_HOME=$HADOOP_INSTALL
ENV HADOOP_HDFS_HOME=$HADOOP_INSTALL
ENV YARN_HOME=$HADOOP_INSTALL
ENV HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_INSTALL/lib/native
ENV HADOOP_OPTS="-Djava.library.path=$HADOOP_INSTALL/lib"
ENV HADOOP_USER_NAME=hdfs
ENV HDFS_NS=hdfs://hdfs

COPY ./hadoop-init.sh /hadoop-init.sh
RUN chmod +x /hadoop-init.sh
ENTRYPOINT ["/hadoop-init.sh"]
