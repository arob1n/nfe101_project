from confluent_kafka import Producer
import sys


def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')


def read_and_produce(file_path, topic):
    conf = {'bootstrap.servers': 'localhost:9092'}
    producer = Producer(conf)

    with open(file_path, 'r') as file:
        for line in file:
            producer.produce(topic, value=line.strip(), callback=delivery_report)
            producer.poll(0)

    producer.flush()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python insert-topics.py <file_path> <kafka_topic>")
        sys.exit(1)

    file_path = sys.argv[1]
    topic = sys.argv[2]

    read_and_produce(file_path, topic)
