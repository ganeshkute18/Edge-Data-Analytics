from azure.iot.device import IoTHubDeviceClient, Message
import os
import random, time

# Optionally load a .env file if python-dotenv is installed. This is non-fatal
# so the script still works if the user prefers to set environment variables
# in their shell.
try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception:
    # python-dotenv not installed or failed to load; continue and rely on env
    pass


def get_connection_string():
    """Return CONNECTION_STRING from environment or raise a clear error.

    The user should add `CONNECTION_STRING=...` to the provided `.env` file or
    export it in their environment before running.
    """
    conn = os.getenv("CONNECTION_STRING")
    if not conn:
        raise RuntimeError(
            "Environment variable CONNECTION_STRING not set. Add it to a .env file as 'CONNECTION_STRING=...' or export it in your environment."
        )
    return conn


def main():
    CONNECTION_STRING = get_connection_string()
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    print("🌍 Edge device simulator started. Sending telemetry to Azure IoT Hub...\n")

    while True:
        temperature = random.uniform(20.0, 35.0)
        humidity = random.uniform(40.0, 80.0)

        # Optional: simple edge-side analytics (local rule)
        if temperature > 30:
            print("⚠️ High temperature detected locally at the edge!")

        msg = Message(f'{{"temperature": {temperature:.2f}, "humidity": {humidity:.2f}}}')
        client.send_message(msg)
        print(f"📤 Sent message: {msg}")
        time.sleep(3)


if __name__ == "__main__":
    main()
