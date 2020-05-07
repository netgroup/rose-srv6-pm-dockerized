import logging
import logging.config
from kafka_logger.handlers import KafkaLoggingHandler

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('ktig')

KAFKA_BOOTSTRAP_SERVER = ('kafka:9092')
TOPIC = 'ktig'

kafka_handler_obj = KafkaLoggingHandler(KAFKA_BOOTSTRAP_SERVER, TOPIC,
                                        security_protocol='PLAINTEXT',
                                        unhandled_exception_logger=logger)

logger.addHandler(kafka_handler_obj)

logger.setLevel(logging.DEBUG)


logger.info({'measure_id': 1, 'interval': 10, 'timestamp': '',
             'color': 'red', 'sender_tx_counter': 50,
             'sender_rx_counter': 50, 'reflector_tx_counter': 48,
             'reflector_rx_counter': 48})   
