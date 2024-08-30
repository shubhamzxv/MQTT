import paho.mqtt.client as mqtt
import ssl

# Connection parameters
aws_iot_endpoint = "a2lqq15sxkfkml-ats.iot.eu-north-1.amazonaws.com"
root_ca = "certificates/root-CA.crt"
certificate = "certificates/mqtt_shubham.cert.pem"
private_key = "certificates/mqtt_shubham.private.key"

def create_client():
	# Create MQTT client
	client = mqtt.Client(client_id="basicPubSub")

	# Enable debug logging
	client.enable_logger()

	# Configure TLS/SSL
	client.tls_set(ca_certs=root_ca,
				   certfile=certificate,
				   keyfile=private_key,
				   cert_reqs=ssl.CERT_REQUIRED,
				   tls_version=ssl.PROTOCOL_TLSv1_2)

	# Define callback functions
	def on_connect(client, userdata, flags, rc):
		if rc == 0:
			print("Connected successfully")
		else:
			print(f"Connect failed with result code {rc}")

	def on_log(client, userdata, level, buf):
		print(f"Log: {buf}")

	def on_disconnect(client, userdata, rc):
		print("Disconnected with result code " + str(rc))

	# Set callback functions
	client.on_connect = on_connect
	client.on_log = on_log
	client.on_disconnect = on_disconnect

	return client