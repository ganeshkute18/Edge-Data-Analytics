
🌐 Edge-to-Cloud Data Analytics using Azure IoT Hub & Power BI

🎯 Objective

Build a basic IoT pipeline that:

Sends sensor data from a Python edge simulator

Sends it to Azure IoT Hub

Processes it using Azure Stream Analytics

Shows live results on a Power BI dashboard



---

🧱 System Flow

Python Sensor Simulator
        ↓
Azure IoT Hub
        ↓
Stream Analytics (Real-time processing)
        ↓
Power BI Dashboard


---

🪜 Steps to Implement

1️⃣ Create Azure Resources

Create a Resource Group → EdgeDemoRG

Region: East US



---

2️⃣ Create IoT Hub

Search → “IoT Hub” → Create

Tier: Free (F1)

Region same as your RG

Enable public network + TLS 1.2



---

3️⃣ Add a Device

IoT Hub → Devices → Add device

Device ID: edge-sensor

Copy the Primary Connection String



---

4️⃣ Create a Python Edge Simulator

Install SDK:

pip install azure-iot-device

Create edge_device.py:

from azure.iot.device import IoTHubDeviceClient, Message
import random, time

CONNECTION_STRING = "YOUR_DEVICE_CONNECTION_STRING"

client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

while True:
    temperature = random.uniform(20, 35)
    humidity = random.uniform(40, 80)

    message = Message(f'{{"temperature": {temperature}, "humidity": {humidity}}}')
    client.send_message(message)

    print("Sent →", message)
    time.sleep(3)

Run:

python3 edge_device.py


---

5️⃣ Check IoT Hub Messages

IoT Hub → Overview → Messages should increase.


---

6️⃣ Create Stream Analytics Job

Add input → IoT Hub

Add output → Power BI

Write query:


SELECT
  AVG(temperature) AS avg_temp,
  AVG(humidity) AS avg_humidity,
  System.Timestamp AS event_time
INTO pbioutput
FROM iotinput
GROUP BY TumblingWindow(second, 10)

Start job.


---

7️⃣ Create Power BI Dashboard

Open Power BI

Dataset → EdgeAnalyticsDataset

Create report

Add charts for avg_temp, avg_humidity


You will see live updates every 10 seconds.


---

🧠 Summary

This project shows a simple end-to-end IoT pipeline:

Python acts as an edge sensor simulator

Azure IoT Hub receives telemetry

Stream Analytics processes the data in real time

Power BI shows live results

Demonstrates the basic concept of edge-to-cloud analytics



---

✍️ Author

Ganesh Kute  

