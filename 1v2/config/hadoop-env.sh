# Set Hadoop-specific environment variables here.

# JAVA_HOME
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

# Hadoop home directory
export HADOOP_HOME=/opt/hadoop

# Hadoop configuration directory
export HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop

# Native library path
export HADOOP_COMMON_LIB_NATIVE_DIR=${HADOOP_HOME}/lib/native

# Hadoop temporary directory
export HADOOP_TMP_DIR=${HADOOP_HOME}/tmp