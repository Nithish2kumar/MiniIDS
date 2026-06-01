# 🛡️ MiniIDS

A lightweight Intrusion Detection System (IDS) built using Python and Scapy for real-time network traffic monitoring and attack detection.

---

## 🚀 Features

- 📡 Real-time packet sniffing
- ⚠️ SYN Flood detection
- 🔍 Port scan detection
- 🚨 Alert generation
- 🧠 TCP packet analysis
- 🐍 Built completely in Python

---

## 🛠️ Technologies Used

- Python 3
- Scapy
- Linux
- Networking Fundamentals

---

## 📂 Project Structure

```bash
MiniIDS/
│
├── ids.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Nithish2kumar/MiniIDS.git
```

Move into project directory:

```bash
cd MiniIDS
```

Install dependencies:

```bash
pip install scapy
```

---

## ▶️ Running the IDS

```bash
sudo python3 miniids.py
```

---

## 🧪 Detection Capabilities

### SYN Flood Detection
Detects excessive SYN packets from a source IP within a specific time window.

### Port Scan Detection
Detects suspicious scanning behavior when multiple ports are targeted rapidly.

---

## 🧠 Concepts Used

- Packet Sniffing
- TCP/IP Analysis
- TCP Flags
- Stateful Detection
- Threshold-Based Alerting
- Real-Time Monitoring

---

## 📸 Example Output

```bash
[SYN] 192.168.1.5 -> 192.168.1.1:80
Count: 11

==================================================
[ALERT] Possible SYN Flood Attack from 192.168.1.5
==================================================
```

---

## 🔮 Future Improvements

- GUI Dashboard
- PCAP File Analysis
- Email Alerts
- Logging System
- Machine Learning Detection
- SCADA Protocol Monitoring

---

## ⚠️ Disclaimer

This project is created strictly for:
- Educational purposes
- Cybersecurity learning
- Lab environment testing

Do not use against unauthorized systems.

---

## 👨‍💻 Author

**NK (Nithish Kumar)**

Cybersecurity and Blockchain Technology Student

---

## ⭐ Support

If you like this project:

- Star the repository
- Fork the project
- Improve and contribute
