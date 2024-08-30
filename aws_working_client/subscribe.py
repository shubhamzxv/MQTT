from mqtt_client import create_client

# Topic to subscribe to
topic = "sdk/test/python"

# Create and configure the client
client = create_client()

# Define callback function for subscribing
def on_message(client, userdata, msg):
	print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

# Set the message callback
client.on_message = on_message

# Connect to the broker
client.connect("a2lqq15sxkfkml-ats.iot.eu-north-1.amazonaws.com", 8883, 60)

# Start the loop
client.loop_start()

# Subscribe to the topic
client.subscribe(topic)

# Keep the script running to listen for messages
try:
	while True:
		pass
except KeyboardInterrupt:
	print("Exiting...")

# Stop the loop and disconnect
client.loop_stop()
client.disconnect()