from kafka import KafkaProducer
from kafka.errors import KafkaError
import json

# produce json messages
producer = KafkaProducer(bootstrap_servers='kafka:9092',  security_protocol='PLAINTEXT',
                         value_serializer=lambda m: json.dumps(m).encode('ascii'))

result = producer.send('ktig', {'measure_id': 1, 'interval': 10, 'timestamp': '',
                                'color': 'red', 'sender_tx_counter': 50,
                                'sender_rx_counter': 50, 'reflector_tx_counter': 48,
                                'reflector_rx_counter': 48})


producer.close()
