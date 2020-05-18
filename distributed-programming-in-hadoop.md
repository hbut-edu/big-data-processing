sudo docker run -p 8088:8088 -p 9000:9000 -v /home/ryu/Documents/hadoop/master/share:/root/share -it -h master --name master ubuntu/hadoop_3.2.1_cluster_tested

sudo docker run -v /home/ryu/Documents/hadoop/worker01/share:/root/share -it -h worker01 --name worker01 ubuntu/hadoop_3.2.1_cluster_tested

sudo docker run -v /home/ryu/Documents/hadoop/worker02/share:/root/share -it -h worker02 --name worker02 ubuntu/hadoop_3.2.1_cluster_tested

=> to docker compose

./bin/hdfs dfs -put /root/share/training_data.csv /input

./bin/hdfs dfs -ls /input

sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

https://github.com/docker/compose/releases

https://docs.docker.com/compose/compose-file/

sudo docker-compose up -d

sudo docker exec -it master bash

sudo docker exec -it worker01 bash

sudo docker exec -it worker02 bash

Q: Pool overlaps with other one on this address space

A: sudo docker network rm <network id>

Q: 删除所有已经退出的容器

A: sudo docker container prune

//TODO JAVA

//TODO Hadoop Streaming

