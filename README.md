# 🌐 Edge-to-Cloud Data Analytics using Azure IoT Hub, Stream Analytics & Power BI

## 🎯 Objective
To build an end-to-end IoT pipeline that:
- Collects sensor data from an **edge device (Python simulator)**.
- Sends data securely to **Azure IoT Hub**.
- Processes it in real time using **Azure Stream Analytics**.
- Displays the processed data on a **live Power BI dashboard**.

---

## 🧱 System Architecture
```
[ Edge Device (Python Simulator) ]
        ↓ (MQTT over TLS 1.2)
[ Azure IoT Hub ]
        ↓
[ Azure Stream Analytics Job ]
        ↓
[ Power BI Dashboard ]
```

---

## 🪜 Implementation Steps

### 🧩 STEP 1: Create Azure Resources
1. Log in to [Azure Portal](https://portal.azure.com).
2. Create a **Resource Group** named `EdgeDemoRG` (Region: East US / West Europe).

### ⚙️ STEP 2: Create IoT Hub
1. Search “IoT Hub” → Create.
2. Set Resource Group: `EdgeDemoRG`, Region: East US, Tier: **Free (F1)**.
3. Networking → Public Access, TLS 1.2.
4. Permission Model → **Shared Access Policy + RBAC**.
5. Assign yourself **IoT Hub Data Contributor**.
6. Review + Create.

### 🪪 STEP 3: Register Device in IoT Hub
1. IoT Hub → **Devices → + New Device**.
2. Device ID: `edge-sensor`, Authentication: **Symmetric Key**.
3. Save and copy **Primary Connection String**.

---

## 🧠 STEP 4: Simulate Edge Device (Python)
Install SDK:
```bash
pip install azure-iot-device
```

Create `edge_device.py`:
```python
from azure.iot.device import IoTHubDeviceClient, Message
import random, time

CONNECTION_STRING = "PASTE_YOUR_DEVICE_CONNECTION_STRING"

def main():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    print("🌍 Edge device simulator started. Sending telemetry to Azure IoT Hub...\n")

    while True:
        temperature = random.uniform(20.0, 35.0)
        humidity = random.uniform(40.0, 80.0)
        if temperature > 30:
            print("⚠️ ALERT: High temperature detected locally at the edge!")
        msg = Message(f'{{"temperature": {temperature:.2f}, "humidity": {humidity:.2f}}}')
        client.send_message(msg)
        print(f"📤 Sent message: {msg}")
        time.sleep(3)

if __name__ == "__main__":
    main()
```

Run:
```bash
python3 edge_device.py
```

✅ Data is now sent securely to Azure IoT Hub using MQTT over TLS.

---

## ☁️ STEP 5: Verify in IoT Hub
- IoT Hub → Overview → “Messages to IoT Hub” should increase.

---

## 🔄 STEP 6: Create Azure Stream Analytics Job
1. Search “Stream Analytics Job” → Create.
2. Name: `EdgeAnalyticsJob`, Resource Group: `EdgeDemoRG`, Region: same as IoT Hub.
3. Streaming Units: 1 → Create.

---

## 📥 STEP 7: Add Input (IoT Hub)
1. Stream Analytics → **Inputs → + Add → IoT Hub**.
2. Alias: `iotinput`.
3. IoT Hub: `EdgeDemoHub`, Consumer group: `edgeanalytics-cg`, Serialization: JSON.

---

## 📤 STEP 8: Add Output (Power BI)
1. Outputs → + Add → Power BI.
2. Authorize with Power BI account.
3. Alias: `pbioutput`, Dataset: `EdgeAnalyticsDataset`, Table: `SensorAverages`.

---

## 🧮 STEP 9: Write Query
```sql
SELECT
    AVG(CAST(temperature AS FLOAT)) AS avg_temp,
    AVG(CAST(humidity AS FLOAT)) AS avg_humidity,
    System.Timestamp AS event_time
INTO
    [pbioutput]
FROM
    [iotinput]
GROUP BY
    TumblingWindow(second, 10)
```

Save → Start Job → “Now”. ✅

---

## 📊 STEP 10: Power BI Live Dashboard
1. Go to [Power BI](https://app.powerbi.com).
2. Open Dataset `EdgeAnalyticsDataset` → **Create Report**.
3. Add:
   - Line Chart → `event_time` (X), `avg_temp`, `avg_humidity` (Y).
   - Card → `avg_temp` for live reading.
4. Watch real-time updates every 10 seconds!

---

## 🧠 Optional: Add Edge Intelligence
Add in your simulator:
```python
if temperature > 30:
    print("⚠️ Local alert: High temperature detected!")
```
✅ Demonstrates local edge-side analytics.

---

## 🧩 Final Architecture Recap
```
[ Python Edge Device ]
   ↓ (MQTT over TLS 1.2)
[ Azure IoT Hub ]
   ↓
[ Azure Stream Analytics ]
   ↓
[ Power BI Dashboard ]
```

---

## ✅ Output Verification
| Step | Check |
|------|--------|
| Python simulator | Console prints telemetry |
| IoT Hub | Message count increases |
| Stream Analytics | Status = Running |
| Power BI | Dashboard updates live |

---

## 🧠  Summary
> This project demonstrates an edge-to-cloud IoT analytics system. A simulated edge device sends data securely to Azure IoT Hub using MQTT over TLS, which is processed in real time by Azure Stream Analytics and visualized in Power BI. It represents real-world industrial IoT data analytics.

---

## 🧾 Author
**Pratham Bhosale**  

