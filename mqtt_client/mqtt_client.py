# mqtt_client.py
import paho.mqtt.client as mqtt

class MQTTClient:
    def __init__(self, broker, port, topic_sub, topic_pub):
        self.broker = broker
        self.port = port
        self.topic_sub = topic_sub
        self.topic_pub = topic_pub
        self.client = mqtt.Client()

        # Assign the callbacks
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_publish = self.on_publish

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected successfully")
            self.client.subscribe(self.topic_sub)
        else:
            print("Connect failed with code", rc)

    def on_message(self, client, userdata, msg):
        print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

    def on_publish(self, client, userdata, mid):
        print("Message published")

    def connect(self):
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_start()

    def publish(self, message):
        self.client.publish(self.topic_pub, message)

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()



