from scapy.all import sniff, IP, TCP , Ether ,UDP,ARP
import time
import json
from collections import defaultdict
from datetime import datetime
import os

# ====== Settings ======
TIME_WINDOW = 10        # seconds
PORT_THRESHOLD = 10     # unique ports in time window
HONEYPOT_PORT = 22222   # fake port

# ====== Data Structure ======
ip_data = defaultdict(lambda: {
    "tcp_ports": set(),
    "udp_ports": set(),
    "arp_requests": set(),
    "first_seen": time.time(),
    "last_seen": time.time(),
    "arp_count": 0,
    "tcp_alerts": 0,
    "udp_alerts": 0
})

# ====== Logging ======
def get_mac(packet):
    if packet.haslayer(Ether):
        return packet[Ether].src
    return "unknown"

blocked = set()

#def block_attacker_ip_mac(ip, mac):
    #if ip not in blocked:
        #os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")
        #os.system(f"sudo iptables -A INPUT -m mac --mac-source {mac} -j DROP")
        #blocked.add(ip)

#def block_attacker_ip(ip):
    #if ip not in blocked:
        #os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")
        #blocked.add(ip)
        
def log_alert(packet,ip, reason, ports=None):
    mac=get_mac(packet)
    if packet.haslayer(ARP):
        #block_attacker_ip_mac(ip, mac)
        print("y")
    else:
        #block_attacker_ip(ip)
        print("s")
        
    log_entry = {
        "Timestamp": datetime.now().isoformat(),
        "IP": ip,
        "MAC":mac,
        "Reason": reason,
        "Details": list(ports) if ports else []
    }

    with open("scan_log.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    with open("alerts.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
# ====== Detection Logic ======
def detect_scan(packet):
    if packet.haslayer(IP) :
        ip = packet[IP].src
        data= ip_data[ip]
        
        current_time = time.time()
        # Reset if time window expired
        if current_time - data["first_seen"] > TIME_WINDOW:
            data["tcp_ports"].clear()
            data["udp_ports"].clear()
            data["first_seen"] = current_time

        # Check SYN only (SYN flag = 0x02)
        if packet.haslayer(TCP):
            tcp=packet[TCP]
            data["tcp_ports"].add(tcp.dport)
            data["last_seen"] = current_time

            # Honeypot detection
            if tcp.dport == HONEYPOT_PORT:
                print(f"[!!!] Honeypot hit from {ip}")
                log_alert(packet,ip, "Honeypot port access", [tcp.dport])

            # Port scan detection
            if len(data["tcp_ports"]) >= PORT_THRESHOLD:
                print(f"[!!!] Port Scan detected from {ip}")
                log_alert(packet,ip, f"Port scan detected ({len(data['tcp_ports'])} ports)",data['tcp_ports'])
                data["tcp_ports"].clear()
                data["tcp_alerts"] += 1
                
        if packet.haslayer(UDP):
            udp=packet[UDP]
            data["udp_ports"].add(udp.dport)
            data["last_seen"] = current_time

            # Port scan detection
            if len(data["udp_ports"]) >= PORT_THRESHOLD:
                print(f"[!!!] Port Scan detected from {ip}")
                log_alert(packet,ip, f"Port scan detected ({len(data['udp_ports'])} ports)",data['udp_ports'])
                data["udp_ports"].clear()
                data["udp_alerts"] += 1
                
        
    if packet.haslayer(ARP):
        mac=get_mac(packet)
        arp = packet[ARP]
        ip = arp.psrc

        data = ip_data[ip]

        current_time = time.time()

        # Reset window
        if current_time - data["first_seen"] >= 1:
            data["arp_count"] = 0
            data["arp_requests"].clear()
            data["first_seen"] = current_time

        # Count unique ARP requests
        data["arp_requests"].add(arp.pdst)
        data["arp_count"] = len(data["arp_requests"])

        if data["arp_count"] >= 5:

            print(f"[!!!] ARP Scan detected from {ip}")

            log_alert(
                packet,
                ip,
                "ARP scan detected",
                list(data["arp_requests"])
            )

            data["arp_requests"].clear()

# ====== Start Sniffing ======
print("Starting IDS...")
sniff(filter="tcp or udp or arp", prn=detect_scan, store=0)