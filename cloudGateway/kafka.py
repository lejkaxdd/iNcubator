from confluent_kafka import Producer
import yaml, os

config_dir = os.path.dirname(os.path.abspath(__file__))
with open(config_dir + '/config.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)
    

kafka_config = {
    'bootstrap.servers': str(config['kafka_service']['KAFKA_SERVER']) + ':' + str(config['kafka_service']['KAFKA_PORT'])
}

for i in range(3):
    print(kafka_config)

producer = Producer(kafka_config)

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
        return True
    else:
        print(f'Message {msg.value().decode('utf-8')} delivered to topic [{msg.topic()}], partition [{msg.partition()}]')
        return False

def sendMessageToTopic(topic, message):
    try:
        producer.produce(topic, value=message, callback=delivery_report)
        producer.flush()
        return True
    except:
        return False
        
