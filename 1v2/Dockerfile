# Use Ubuntu 22.04 as the base image
FROM ubuntu:22.04

# Set environment variables
ENV HADOOP_HOME=/opt/hadoop
ENV HADOOP_MAPRED_HOME=$HADOOP_HOME
ENV HADOOP_VERSION=3.3.4
ENV HDFS_NAMENODE_USER=root
ENV HDFS_DATANODE_USER=root
ENV HDFS_SECONDARYNAMENODE_USER=root
ENV YARN_RESOURCEMANAGER_USER=root
ENV YARN_NODEMANAGER_USER=root
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

# Install necessary packages
RUN apt-get update && apt-get install -y openjdk-8-jdk wget openssh-server openssh-client nano net-tools

# Generate SSH key 无密码访问
RUN ssh-keygen -t rsa -f /root/.ssh/id_rsa -N '' && \
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

# Download and install Hadoop
RUN wget https://downloads.apache.org/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz && \
    tar -xzf hadoop-${HADOOP_VERSION}.tar.gz -C /opt && \
    mv /opt/hadoop-${HADOOP_VERSION} ${HADOOP_HOME} && \
    rm hadoop-${HADOOP_VERSION}.tar.gz

# Copy Hadoop configuration files
COPY config/core-site.xml ${HADOOP_HOME}/etc/hadoop/core-site.xml
COPY config/hdfs-site.xml ${HADOOP_HOME}/etc/hadoop/hdfs-site.xml
COPY config/mapred-site.xml ${HADOOP_HOME}/etc/hadoop/mapred-site.xml
COPY config/yarn-site.xml ${HADOOP_HOME}/etc/hadoop/yarn-site.xml
COPY config/hadoop-env.sh ${HADOOP_HOME}/etc/hadoop/hadoop-env.sh

# 创建Hadoop数据目录
RUN mkdir -p $HADOOP_HOME/hdfs/data/namenode && \
    mkdir -p $HADOOP_HOME/hdfs/data/datanode

# Format Hadoop NameNode
RUN ${HADOOP_HOME}/bin/hdfs namenode -format

# Expose necessary ports
EXPOSE 9000 9870 9866 9867 19888 8088 8030 8031 8032 8033 8040 8042 22

RUN rm /tmp/hadoop-root-namenode.pid
RUN mkdir -p /run/sshd