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
# Smart Intrusion Detection and Security System

## Overview

Smart Intrusion Detection and Security System is an integrated security solution that combines physical security and network security into one platform.

The system uses Raspberry Pi, a PIR Motion Sensor, and Face Recognition technology to monitor physical environments and detect unauthorized individuals. At the same time, it monitors network activities to identify suspicious behavior such as port scanning, ARP scanning, and other intrusion attempts.

When a threat is detected, the system can capture evidence, send alerts, and store information for further investigation.

---

## Problem Statement

Traditional security systems usually focus on only one aspect of security.

Some systems monitor physical access using cameras and sensors but cannot detect cyber attacks.

Others monitor network traffic but cannot identify unauthorized physical access.

This creates a security gap where attackers can exploit either the physical environment or the network infrastructure.

---

## Proposed Solution

Our solution integrates both physical and network security into a single intelligent system.

### Physical Security

* Motion detection using PIR Sensor.
* Face recognition for identifying authorized users.
* Detection of unknown individuals.
* Automatic image capture of intruders.
* Sending captured data to the server.

### Network Security

* Monitoring network traffic.
* Detecting Port Scanning attacks.
* Detecting ARP Scanning activities.
* Honeypot-based intrusion detection.
* Logging suspicious activities.
* Automatic blocking of malicious IP addresses.

---

## System Architecture

1. PIR Sensor detects movement.
2. Raspberry Pi activates the camera.
3. Face Recognition identifies the detected person.
4. If the person is unknown:

   * Capture image.
   * Send image to server.
   * Generate alert.
5. IDS continuously monitors network traffic.
6. Suspicious activities are detected and logged.
7. Malicious IPs can be blocked automatically.

---

## Technologies Used

### Hardware

* Raspberry Pi
* PIR Motion Sensor
* Raspberry Pi Camera Module

### Software

* Python
* OpenCV
* Face Recognition Library
* Flask
* Requests
* Base64 Encoding
* IDS Components
* Firewall Rules

---

## Features

* Real-time motion detection.
* Real-time face recognition.
* Unknown person detection.
* Image capture and transmission.
* Intrusion Detection System (IDS).
* Port Scan Detection.
* ARP Scan Detection.
* Honeypot Monitoring.
* Alert Generation.
* Automatic Threat Response.

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/project-name.git
cd project-name
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Authorized Faces

Place images of authorized users inside:

```text
known_faces/
```

Example:

```text
known_faces/
├── Ahmed.jpg
├── Ali.jpg
├── Ezzat.jpg
```

### 4. Configure Webhook URL

Open the main script and update:

```python
WEBHOOK_URL = "YOUR_SERVER_URL/upload"
```

### 5. Start Flask Server

```bash
python server.py
```

### 6. Start Main Security System

```bash
python main.py
```

### 7. Start IDS Module

```bash
python ids.py
```

---

## Usage

1. The PIR sensor detects motion.
2. The camera starts automatically.
3. Face recognition identifies the person.
4. Unknown individuals are recorded and reported.
5. Network traffic is continuously monitored.
6. Intrusion attempts are detected and logged.
7. Security alerts are generated when threats are found.

---

## Future Improvements

* Mobile application integration.
* Cloud storage support.
* AI-based anomaly detection.
* Multi-camera support.
* Real-time dashboard.
* Advanced threat intelligence integration.

---

## Project Goal

The main goal of this project is to provide a low-cost intelligent security platform capable of protecting both physical environments and computer networks through automation, monitoring, and threat detection.

