import json
import time
import firebase_admin
from firebase_admin import credentials, messaging

# ==== إعداد Firebase ====
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# ==== ملف الديتكشن ====
FILE_PATH = "alerts.json"
open(FILE_PATH,"w").close

last_timestamp = None

def send_to_firebase(data):

    message = messaging.Message(

        notification=messaging.Notification(
            title="Network Alert",
            body=f"{data['Reason']} from {data['IP']}"
        ),

        # 🔴 البيانات اللي Flutter هيقراها
        data={
            "IP": str(data["IP"]),
            "MAC": str(data["MAC"]),
            "Reason": str(data["Reason"]),
            "Timestamp": str(data["Timestamp"])
        },

        topic="ids_alerts"
    )

    response = messaging.send(message)
    print("Successfully sent message:", response)


while True:
    try:

        with open(FILE_PATH, "r") as f:
            lines = f.readlines()

            if not lines:
                time.sleep(1)
                continue

            last_line = lines[-1]
            data = json.loads(last_line)

            timestamp = data["Timestamp"]

            if timestamp != last_timestamp:

                send_to_firebase(data)

                last_timestamp = timestamp

    except Exception as e:
        print("Error:", e)

    time.sleep(1)