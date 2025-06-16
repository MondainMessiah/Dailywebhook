import requests
import time
import os

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

COMMANDS = [
    "/boosted boss",
    "/boosted creature",
    "/rashid",
    "/event list"
]

def send_webhook():
    for command in COMMANDS:
        data = {"content": command}
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code in [200, 204]:
            print(f"Sent: {command}")
        else:
            print(f"Failed to send '{command}': {response.status_code} - {response.text}")
        time.sleep(1)

if __name__ == "__main__":
    send_webhook()
