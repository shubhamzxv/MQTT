# AWS IoT Core and MQTT Client Setup

This guide will help you set up AWS IoT Core and an MQTT client on your device. The setup is divided into two parts: configuring AWS IoT Core and setting up the MQTT client.

## Part 1: AWS IoT Core Setup

### Step 1: Create an AWS Account
1. Go to [AWS](https://aws.amazon.com/) and create a new account if you don't have one.
2. Log in to the AWS Management Console.

### Step 2: Create an IoT Thing
1. Navigate to the AWS IoT Core service.
2. In the left-hand menu, click on **Manage** and then **Things**.
3. Click on **Create** and follow the prompts to create a new IoT Thing.

### Step 3: Create and Attach a Policy
1. In the AWS IoT Core console, go to **Secure** and then **Policies**.
2. Click on **Create** to create a new policy.
3. Define the policy with the necessary permissions for your IoT Thing.
4. Attach the policy to the certificate created in the next step.

### Step 4: Create and Download Certificates
1. In the AWS IoT Core console, go to **Secure** and then **Certificates**.
2. Click on **Create** to create a new certificate.
3. Download the certificate, private key, and root CA certificate.
4. Attach the certificate to your IoT Thing.

### Step 5: Configure the Device
1. Copy the downloaded certificates and keys to your device.
2. Note down the endpoint URL from the AWS IoT Core console.

## Part 2: MQTT Client Setup

### Step 1: Install Paho MQTT Client
1. Open a terminal on your device.
2. Install the Paho MQTT client using pip:
   ```sh
   pip install paho-mqtt