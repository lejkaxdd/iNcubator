from confluent_kafka import Consumer, KafkaException, KafkaError
import yaml, os, requests

config_dir = os.path.dirname(os.path.abspath(__file__))
with open(config_dir + '/config.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)
    

kafka_config = {
    'bootstrap.servers': str(config['kafka_service']['KAFKA_SERVER']) + ':' + str(config['kafka_service']['KAFKA_PORT']),
    'group.id' : 'subscriptionServiceGroup',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(kafka_config)

topic = config['kafka_service']['KAFKA_TOPIC_NAME']
consumer.subscribe([topic])

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print(f'End of partition {msg.topic()} [{msg.partition()}]')
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            print(f'Message received: {msg.value().decode("utf-8")}')
            req = requests.post('http://subscriptionService:8083/api/v1/consumer/subscriptions', json=msg.value().decode("utf-8"))
            print(req)
            
            
finally:
    consumer.close()