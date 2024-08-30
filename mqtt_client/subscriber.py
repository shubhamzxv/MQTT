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

# The script will keep running, waiting for messages
try:
    while True:
        pass  # Keep the script running to receive messages
except KeyboardInterrupt:
    print("Disconnecting from broker")
    mqtt_client.disconnect()
