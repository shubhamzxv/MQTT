import json
from mqtt_client import create_client

# Topic to publish to
topic = "sdk/test/python"

# Create and configure the client
client = create_client()

# Define callback function for publishing
def on_publish(client, userdata, mid):
	print("Message Published...")

# Set the publish callback
client.on_publish = on_publish

# Connect to the broker
client.connect("a2lqq15sxkfkml-ats.iot.eu-north-1.amazonaws.com", 8883, 60)

# Start the loop
client.loop_start()

message = {
	"message": "Hello from Python!",
	"timestamp": "2023-10-05T12:00:00Z"
}
try:
	result = client.publish(topic, json.dumps(message), qos=1)
	status = result[0]
	if status == 0:
		print("Message sent successfully")
	else:
		print(f"Failed to send message, result code {status}")
except Exception as e:
	print(f"An error occurred: {e}")

# Stop the loop and disconnect
client.loop_stop()
client.disconnect()