# 🛡️ Smart Intrusion Detection and Security System (SIDS)

## 📸 Project Result

![Intrusion Detection Result](assets/test_image.jpg)

📁 File Name: `test_image.jpg`

---

## 📌 Overview

Smart Intrusion Detection and Security System is an integrated security solution that combines **physical security** and **network security** into one intelligent platform.

The system uses:
- Raspberry Pi
- PIR Motion Sensor
- Face Recognition (Python + OpenCV)
- Intrusion Detection System (IDS)

to detect unauthorized access and suspicious network activities in real time.

---

## 🧠 How It Works

### 🔹 Physical Security
- Motion detection using PIR sensor
- Face recognition for authorized users
- Capture image of unknown persons
- Send alerts to server

### 🔹 Network Security
- Monitor network traffic
- Detect port scanning
- Detect ARP scanning
- Log suspicious activities
- Block malicious IPs
- <img width="768" height="1365" alt="صور تيست المشروع وفى كشف الشخص الغريب " src="https://github.com/user-attachments/assets/e43f26d5-1c5b-4553-b584-b95f79e89963" />



---

## 💻 Code Example (Face Recognition)

```python
import face_recognition

# Load image
image = face_recognition.load_image_file("test_image.jpg")

# Detect faces
face_locations = face_recognition.face_locations(image)

print("Faces found:", face_locations)
