# MQTT

for testing the pub/sub

mosquitto_sub -h test.mosquitto.org -t "test/topic/pub"

mosquitto_pub -h test.mosquitto.org -t "test/topic/sub" -m "Hello from another client"