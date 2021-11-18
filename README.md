# kafka-app

cd /usr/hdp/current/kafka-broker

# list of all topics
bin/kafka-topics.sh --list --zookeeper localhost:2181

# create topics
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic random_data

# delete topic
bin/kafka-topics.sh --delete --zookeeper localhost:2181 --topic random_data

# get detail of topics
bin/kafka-topics.sh --describe --zookeeper localhost:2181 --topic randomdata

# get number of msg in topics
bin/kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list 172.18.0.2:6667 --topic randomdata --time -1








