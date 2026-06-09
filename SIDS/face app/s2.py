import cv2
import face_recognition
import os
import time
import RPi.GPIO as GPIO
from picamera2 import Picamera2
import uuid
import requests
import base64

# ===== Webhook URL (ngrok) =====
WEBHOOK_URL = "https://smolder-recent-uncrushed.ngrok-free.dev/upload"

# ===== PIR Sensor Setup =====
PIR_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

# ===== Send to Webhook =====
def send_to_webhook(frame):

    filename = f"unknown_{uuid.uuid4()}.jpg"

    # حفظ الصورة
    cv2.imwrite(filename, frame)

    # تحويل إلى Base64
    with open(filename, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    # إرسال للسيرفر
    try:
        requests.post(WEBHOOK_URL, json={
            "status": "unknown",
            "image": encoded,
            "time": str(time.time())
        })
        print("📡 Sent to webhook")
    except Exception as e:
        print("❌ Error sending:", e)

    # حذف الصورة من الجهاز
    os.remove(filename)

# ===== Load Known Faces =====
known_encodings = []
known_names = []

BASE_PATH = "/home/pi/Desktop/SIDS/known_faces"

for file in os.listdir(BASE_PATH):
    image = face_recognition.load_image_file(
        os.path.join(BASE_PATH, file)
    )
    enc = face_recognition.face_encodings(image)
    if len(enc) > 0:
        known_encodings.append(enc[0])
        known_names.append(file.split(".")[0])

print("System Ready")

# ===== Camera Setup =====
picam2 = Picamera2()

camera_running = False
last_motion_time = 0
last_sent_time = 0

MOTION_TIMEOUT = 10

try:
    while True:

        motion = GPIO.input(PIR_PIN)

        # حركة
        if motion:
            last_motion_time = time.time()

            if not camera_running:
                print("Camera Started")
                picam2.start()
                camera_running = True

        if camera_running:

            frame = picam2.capture_array()

            small_frame = cv2.resize(frame, (0,0), fx=0.3, fy=0.3)
            rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(rgb_frame)
            encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            name = "Unknown"

            if len(encodings) > 0 and len(known_encodings) > 0:
                distances = face_recognition.face_distance(
                    known_encodings,
                    encodings[0]
                )

                best_match = distances.argmin()

                if distances[best_match] < 0.65:
                    name = known_names[best_match]

            # ===== Unknown Trigger =====
            if name == "Unknown" and len(face_locations) > 0:
                if time.time() - last_sent_time > 5:
                    send_to_webhook(frame)
                    last_sent_time = time.time()

            # ===== Draw =====
            for (top, right, bottom, left) in face_locations:

                top *= 3
                right *= 3
                bottom *= 3
                left *= 3

                cv2.rectangle(frame,
                              (left, top),
                              (right, bottom),
                              (0,255,0), 2)

                cv2.putText(frame,
                            name,
                            (left, top - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8,
                            (0,255,0), 2)

            cv2.imshow("Camera", frame)
            cv2.waitKey(1)

            # إيقاف الكاميرا
            if time.time() - last_motion_time > MOTION_TIMEOUT:
                print("Camera Stopped")
                picam2.stop()
                camera_running = False
                cv2.destroyAllWindows()

        time.sleep(0.05)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
    cv2.destroyAllWindows()