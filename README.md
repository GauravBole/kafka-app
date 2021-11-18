cd /usr/hdp/current/kafka-broker

# list of all topics
bin/kafka-topics.sh --list --zookeeper localhost:2181

# create topics
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic random_data

# delete topic
bin/kafka-topics.sh --delete --zookeeper localhost:2181 --topic random_data

# get detail of topics
bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic randomdata

# get number of messages in topics
bin/kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list 172.18.0.2:6667 --topic randomdata --time -1

# change no of partitions in topics
bin/kafka-topics.sh --zookeeper localhost:2181 --alter --topic randomdata --partitions 2 

``producer can select partitions of therir choice in topic where it want to publish message. But if we want we can send msg to perticular partaion``

# get list of consumer group
bin/kafka-consumer-groups.sh  --list --bootstrap-server 172.18.0.2:6667

# specific consumer detail 
bin/kafka-consumer-groups.sh --describe --group ConsumerGroupA --members --bootstrap-server 172.18.0.2:6667

# detailed consumer info with messages consumed
bin/kafka-consumer-groups.sh --describe --group ConsumerGroupA --bootstrap-server 172.18.0.2:6667










