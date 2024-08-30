from mqtt_client import MQTTClient

# Define MQTT broker details
BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC_PUB = "test/topic/pub"
TOPIC_SUB = "test/topic/sub"

# Create an MQTT client instance
mqtt_client = MQTTClient(BROKER, PORT, TOPIC_SUB, TOPIC_PUB)

# Connect to the broker
mqtt_client.connect()

# Publish a message
message = "Hello from publisher"
mqtt_client.publish(message)

# Disconnect from the broker
mqtt_client.disconnect()
