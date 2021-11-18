from kafka import KafkaConsumer
from kafka.consumer import group
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "randomdata",
        bootstrap_servers= ["172.18.0.2:6667"],
        group_id="ConsumerGroupA"
    )
    print("consumer started")
    for i in consumer:
        print(f"consumer data {json.loads(i.value)}")
