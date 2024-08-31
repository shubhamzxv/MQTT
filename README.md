# MQTT_Client

This project demonstrates a simple MQTT client using the Paho MQTT library in Python. It includes a publisher and a subscriber to test the publish-subscribe mechanism using the Mosquitto broker.

## Prerequisites

- Python 3.x
- Paho MQTT library
- Mosquitto broker

## Installation

1. **Clone the repository**:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Install the Paho MQTT library**:
    ```sh
    pip install paho-mqtt
    ```

3. **Install Mosquitto broker**:
    ```sh
    sudo apt-get update
    sudo apt-get install mosquitto mosquitto-clients
    ```

## Usage

### Publisher

1. **Run the publisher script**:
    ```sh
    python publisher.py
    ```

   This will connect to the Mosquitto broker and publish a message to the specified topic.

### Subscriber

1. **Run the subscriber script**:
    ```sh
    python subscriber.py
    ```

   This will connect to the Mosquitto broker and wait for messages on the specified topic.

## Testing with Mosquitto

1. **Start the Mosquitto broker**:
    ```sh
    mosquitto
    ```

2. **Run the subscriber script**:
    ```sh
    python subscriber.py
    ```

3. **Run the publisher script**:
    ```sh
    python publisher.py
    ```

4. **Verify the output**:
   - The subscriber should print the message received from the publisher.

## Files

- [`mqtt_client.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshubhamkumar%2FShubham%20Kumar%2FTestCode%2FMQTT%2Fmqtt_client%2Fmqtt_client.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/home/shubhamkumar/Shubham Kumar/TestCode/MQTT/mqtt_client/mqtt_client.py"): Contains the [`MQTTClient`](command:_github.copilot.openSymbolFromReferences?%5B%22MQTTClient%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fshubhamkumar%2FShubham%20Kumar%2FTestCode%2FMQTT%2Fmqtt_client%2Fpublisher.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fshubhamkumar%2FShubham%2520Kumar%2FTestCode%2FMQTT%2Fmqtt_client%2Fpublisher.py%22%2C%22path%22%3A%22%2Fhome%2Fshubhamkumar%2FShubham%20Kumar%2FTestCode%2FMQTT%2Fmqtt_client%2Fpublisher.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A24%7D%7D%2C%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fshubhamkumar%2FShubham%20Kumar%2FTestCode%2FMQTT%2Fmqtt_client%2Fsubscriber.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fshubhamkumar%2FShubham%2520Kumar%2FTestCode%2FMQTT%2Fmqtt_client%2Fsubscriber.py%22%2C%22path%22%3A%22%2Fhome%2Fshubhamkumar%2FShubham%20Kumar%2FTestCode%2FMQTT%2Fmqtt_client%2Fsubscriber.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A24%7D%7D%2C%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2Fhome%2Fshubhamkumar%2FShubham%20Kumar%2FTestCode%2FMQTT%2Fmqtt_client%2Fmqtt_client.py%22%2C%22external%22%3A%22file%3A%2F%2F%2Fhome%2Fshubhamkumar%2FShubham%2520Kumar%2FTestCode%2FMQTT%2Fmqtt_client%2Fmqtt_client.py%22%2C%22path%22%3A%22%2Fhome%2Fshubhamkumar%2FShubham%20Kumar%2FTestCode%2FMQTT%2Fmqtt_client%2Fmqtt_client.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A6%7D%7D%5D%5D "Go to definition") class which handles the connection, publishing, and subscribing to the MQTT broker.
- [`publisher.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshubhamkumar%2FShubham%20Kumar%2FTestCode%2FMQTT%2Fmqtt_client%2Fpublisher.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/home/shubhamkumar/Shubham Kumar/TestCode/MQTT/mqtt_client/publisher.py"): Script to publish messages to the MQTT broker.
- [`subscriber.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fshubhamkumar%2FShubham%20Kumar%2FTestCode%2FMQTT%2Fmqtt_client%2Fsubscriber.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/home/shubhamkumar/Shubham Kumar/TestCode/MQTT/mqtt_client/subscriber.py"): Script to subscribe to the MQTT broker and receive messages.

## License
This project is licensed under the MIT License.






# MQTT_Client_for_AWS_IoT_Core

This project demonstrates how to create an MQTT client in Python and connect it to the AWS IoT Core broker. The project includes scripts for publishing and subscribing to messages on a specified topic.

## Project Structure

- `mqtt_client.py`: Contains the logic for creating and configuring the MQTT client.
- `publish.py`: Script to publish messages to a specified topic.
- `subscribe.py`: Script to subscribe to a specified topic and receive messages.

## Prerequisites

- Python 3.x
- `paho-mqtt` library
- AWS IoT Core setup with appropriate certificates

## Setup

1. **Install the required Python library:**

    ```sh
    pip install paho-mqtt
    ```

2. **AWS IoT Core Certificates:**

    Ensure you have the following certificates from AWS IoT Core:
    - Root CA certificate
    - Device certificate
    - Private key

    Place these certificates in a directory named `certificates`:
    - `certificates/root-CA.crt`
    - `certificates/mqtt_shubham.cert.pem`
    - `certificates/mqtt_shubham.private.key`

    **Note:** The actual certificates are not included in this repository for security reasons.

## Usage

### MQTT Client Configuration

The `mqtt_client.py` file contains the configuration for the MQTT client, including setting up the connection parameters, enabling TLS/SSL, and defining callback functions for connection, logging, and disconnection events.

### Publishing Messages

The `publish.py` script is used to publish messages to a specified topic. It configures the MQTT client, connects to the broker, and sends a message in JSON format to the specified topic.

### Subscribing to Messages

The `subscribe.py` script is used to subscribe to a specified topic and receive messages. It configures the MQTT client, connects to the broker, subscribes to the topic, and prints any received messages.

## Running the Scripts

1. **Publish a message:**

    ```sh
    python publish.py
    ```

2. **Subscribe to a topic:**

    ```sh
    python subscribe.py
    ```

## Conclusion

This project provides a basic example of how to create an MQTT client in Python and connect it to AWS IoT Core. You can extend this project by adding more functionality or integrating it with other AWS services.