# HDFS基本操作实验

## HDFS的基本命令格式

```
hdfs dfs -cmd <args>
```

注意：需要事先将HADOOP_HOME/bin目录配置进入环境变量。

## 列出当前目录下的文件

```
hdfs dfs -ls
```

## 在HDFS创建文件夹

```
hdfs dfs -mkdir <文件夹名称>
```

## 级联创建一个文件夹，类似这样一个目录：/mybook/input

```
hdfs fs -mkdir -p <文件夹名称>
```


## 上传文件至HDFS

```
hdfs dfs -put <源路径> <目标存放路径>
```

## 从HDFS上下载文件

```
hdfs dfs -get <HDFS文件路径> <本地存放路径>
```

## 查看HDFS上某个文件的内容

```
hdfs dfs -text <HDFS上的文件存放路径>

hdfs dfs -cat <HDFS上的文件存放路径>
```

## 统计目录下各文件的大小（单位：字节B）

```
hdfs dfs -du <目录路径>
```

## 删除HDFS上某个文件或者文件夹

```
hdfs dfs -rm <文件>

hdfs dfs -rm -r <文件夹>
```

## 使用help命令寻求帮助。

```
hdfs dfs -help <命令>
```