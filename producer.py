from kafka import KafkaProducer
import json
import time
from data_generator import get_random_data

def json_serializer(data):
    """ serilaize and endcode data """
    
    return json.dumps(data).encode('utf-8')


# send data to specific partition
def get_partitioner(key_bytes, all_partitions, available_partitions):
    return 1

# partitioner is optional if we want to publish message to perticular partation only.
producer = KafkaProducer(bootstrap_servers=["172.18.0.2:6667"],
                         value_serializer=json_serializer,
                         partitioner=get_partitioner)

if __name__ == "__main__":
    while True:
        random_data = get_random_data()
        print(random_data)
        producer.send(topic="randomdata", value=random_data)
        time.sleep(3)




