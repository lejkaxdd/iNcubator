#!/bin/sh

# Remove the requirement for KAFKA_ZOOKEEPER_CONNECT
sed -i '/KAFKA_ZOOKEEPER_CONNECT/d' /etc/confluent/docker/configure

# Prevent the startup script from checking for ZooKeeper readiness
sed -i 's/cub zk-ready/echo ignore zk-ready/' /etc/confluent/docker/ensure

# Format the Kafka storage if needed
echo "kafka-storage format --ignore-formatted -t NDU1Nzg2YmVkZjNlNDlkY2 -c /etc/kafka/kafka.properties" >> /etc/confluent/docker/ensure