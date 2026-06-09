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


# 🛡️ Smart Intrusion Detection and Security System (SIDS)

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Status](https://img.shields.io/badge/Status-Completed-green)
![Security](https://img.shields.io/badge/Cyber-Security-red)
![IoT](https://img.shields.io/badge/IoT-RaspberryPi-orange)

---

## 📌 Project Description

SIDS is an intelligent security system that combines both physical security and network security into a single unified platform.

It detects:
- Physical intrusions using sensors + face recognition  
- Network attacks using IDS monitoring  

---

## 📸 Project Preview

![Project Result](assets/test_image.jpg)

📁 File: `test_image.jpg`

---

## ❗ Problem Statement

Modern security systems are usually split into two separate domains:

- Physical security systems (cameras, sensors, alarms)
- Cyber security systems (network monitoring, intrusion detection)

This separation creates several critical issues:

- Security gaps between physical and digital environments  
- Lack of unified monitoring and response system  
- Delayed detection of combined or multi-layer attacks  
- Limited intelligence in traditional surveillance systems  
- No real-time correlation between physical events and network activity  

As a result, attackers can exploit weaknesses in one layer without being detected by the other.

---

## 💡 Solution

This project solves these problems by building a unified intelligent security system that integrates both layers in real time.

The system combines:

- Motion detection using PIR sensors  
- Face recognition for identity verification  
- Intruder image capturing and logging  
- Network intrusion detection (IDS)  
- Real-time alert generation  

All components work together to provide faster and smarter security decisions.

---

## ⚠️ Challenges & Solutions

- Large file uploads on GitHub → removed unnecessary files and added `.gitignore`
- Embedded repository issue → fixed by removing nested git repo
- Secret exposure risk → removed sensitive service account files
- Push conflicts → resolved by cleaning and reinitializing repository

---

## 🚀 Features

- Real-time motion detection  
- Face recognition system  
- Intruder image capture  
- IDS network monitoring  
- Port scan detection  
- ARP scan detection  
- Alert system  
- Automatic threat logging  

---

## 🧰 Tech Stack

- Python 🐍  
- OpenCV 👁️  
- face_recognition library  
- Flask 🌐  
- Raspberry Pi 🍓  
- Networking / IDS tools  
- JSON logging system  

---

## 📁 Project Structure

```bash
SIDS/
├── face app/
├── known_faces/
├── assets/
│   └── test_image.jpg
├── ids.py
├── send_alert.py
├── server.py
├── alerts.json
├── scan_log.json
---


