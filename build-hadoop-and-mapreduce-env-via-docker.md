# 基于docker搭建hadoop与MapReduce

本文扩展自：

http://dblab.xmu.edu.cn/blog/1233/

# 安装docker

## 宿主环境确认

`lsb_release -a`

本文所用环境如下

`发行版版本：Ubuntu 18.04.4 LTS`

`内核版本号：5.3.0-46-generic`

## 整备安装环境

更新系统

`sudo apt update`

`sudo apt upgrade`

下载curl

`sudo apt install curl`

## 安装docker

`curl -fsSL https://get.docker.com -o get-docker.sh`

`sudo sh get-docker.sh`

确认docker的安装

`sudo docker version`

（可选）安装docker-compose

`sudo curl -L "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`

`sudo chmod +x /usr/local/bin/docker-compose`

（重要）添加国内的docker镜像CDN

`sudo vi /etc/docker/daemon.json`

```
{
    "registry-mirrors": ["https://kfp63jaj.mirror.aliyuncs.com","https://docker.mirrors.ustc.edu.cn","https://registry.docker-cn.com","http://hub-mirror.c.163.com"]
}
```

重载docker让CDN配置生效

`sudo systemctl daemon-reload`

`sudo systemctl restart docker`

## 测试docker是否能够抓取镜像和运行

`sudo docker run hello-world`

可以看到hello-world的运行记录

`sudo docker ps -a`

# 基于docker搭建hadoop与MapReduce

## 整备容器环境

抓取ubuntu 18.04的镜像作为基础搭建hadoop环境

`sudo docker pull ubuntu:18.04`

查看镜像是否抓取成功

`sudo docker images`

使用该ubuntu镜像启动一个容器

`docker run -it -v /<host-share-path>/build:/<container-share-path>/build ubuntu`

容器启动后，会自动进入容器的控制台
在容器的控制台安装所需软件

`apt-get update`

`apt-get upgrade`

仅需要vim和ssh

`apt-get install vim openssh-server`

## 配置ssh服务器

让ssh服务器自动启动

`vi ~/.bashrc`

在文件的最末尾加上

`/etc/init.d/ssh start`

让修改即刻生效

`source ~/.bashrc`

配置ssh的无密码访问

`cd ~/.ssh`

`ssh-keygen -t rsa`

`cat id_rsa.pub >> authorized_keys`

## 安装JDK 8

（注意）hadoop目前仅支持jdk 8

`apt-get install openjdk-8-jdk`

`vi ~/.bashrc`

在文件的最末尾加上

```
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
export PATH=$PATH:$JAVA_HOME/bin
```

让jdk配置即刻生效

`source ~/.bashrc`

## 保存镜像

`docker login`

查询CONTAINER ID

`docker ps`

`docker commit <CONTAINER ID> <IMAGE NAME>`

## 安装hadoop

在宿主控制台上下载hadoop二进制压缩包

`cd /<host-share-path>/build`

`wget https://www.apache.org/dyn/closer.cgi/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz`

在容器控制台上解压hadoop

`cd /<container-share-path>/build`

`tar -zxvf hadoop-3.2.1.tar.gz -C /usr/local`

安装完成了，查看hadoop版本

`cd /usr/local/hadoop-3.2.1`

`./bin/hadoop version`

## 为hadoop指定jdk位置

`vi etc/hadoop/hadoop-env.sh`

查找到被注释掉的JAVA_HOME配置位置，更改为：

`export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/`

## hadoop联机配置

配置core-site.xml文件

`vi etc/hadoop/core-site.xml`

加入

```
<configuration>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>file:/usr/local/hadoop-3.2.1/tmp</value>
        <description>Abase for other temporary directories.</description>
    </property>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://master:9000</value>
        </property>
</configuration>
```

配置hdfs-site.xml文件

`vi etc/hadoop/hdfs-site.xml`

加入

```
<configuration>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>file:/usr/local/hadoop-3.2.1/namenode_dir</value>
    </property>
    <property>
        <name>dfs.datanode.data.dir</name>
        <value>file:/usr/local/hadoop-3.2.1/datanode_dir</value>
    </property>
    <property>
        <name>dfs.replication</name>
        <value>3</value>
    </property>
</configuration>
```

## MapReduce配置

配置mapred-site.xml文件

`vi etc/hadoop/mapred-site.xml`

加入

```
  <configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
  </configuration>
```
 
配置yarn-site.xml文件

`vi etc/hadoop/yarn-site.xml`

加入

```
 <configuration>
  <!-- Site specific YARN configuration properties -->
        <property>
            <name>yarn.nodemanager.aux-services</name>
            <value>mapreduce_shuffle</value>
        </property>
        <property>
            <name>yarn.resourcemanager.hostname</name>
            <value>master</value>
        </property>
  </configuration>
```

## 服务启动权限配置

配置start-dfs.sh与stop-dfs.sh文件

```
HDFS_DATANODE_USER=root
HADOOP_SECURE_DN_USER=hdfs
HDFS_NAMENODE_USER=root
HDFS_SECONDARYNAMENODE_USER=root
```

配置start-yarn.sh与stop-yarn.sh文件

```
YARN_RESOURCEMANAGER_USER=root
HADOOP_SECURE_DN_USER=yarn
YARN_NODEMANAGER_USER=root
```

配置完成，保存镜像。

`docker ps`

`docker commit <CONTAINER ID> <IMAGE NAME>`

## 启动hadoop，并进行网络配置

打开三个宿主控制台，启动一主两从三个容器

master

`docker run -it -h master --name master <IMAGE NAME>`

worker01

`docker run -it -h worker01 --name worker01 <IMAGE NAME>`

worker02

`docker run -it -h worker02 --name worker02 <IMAGE NAME>`

分别打开三个容器的/etc/hosts，将彼此的ip地址与主机名的映射信息补全（三个容器均需要如此配置）

`vi /etc/hosts`

添加信息

```
172.18.0.2      master
172.18.0.3      worker01
172.18.0.4      worker02
```

检查配置是否有效

```
ssh master
ssh worker01
ssh worker02
```

在master容器上配置worker容器的主机名

`cd /usr/local/hadoop-3.2.1`

`vi etc/hadoop/worker`

删除`localhost`，加入

```
worker01
worker02
```

网络配置完成

## 启动hadoop

在master主机上

`cd /usr/local/hadoop-3.2.1`

`./bin/hdfs namenode -format`

`./sbin/start-all.sh`

建立一个目录存放配置文件

`./bin/hdfs dfs -mkdir -p /home/hadoop/input`

`./bin/hdfs dfs -put ./etc/hadoop-3.2.1/*.xml /home/hadoop/input`

查看复制是否正常

`./bin/hdfs dfs -ls /home/hadoop/input`

## 运行MapReduce自带的示例程序

`./bin/hadoop jar ./share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar grep /home/hadoop/input output 'dfs[a-z.]+'`

运行结束后，查看输出结果

`./bin/hdfs dfs -cat output/*`