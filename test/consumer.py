from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
        'ktig', bootstrap_servers=['localhost:9092'])
print(consumer)
for m in consumer:
    print(m.value)