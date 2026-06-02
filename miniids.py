from scapy.all import *
from collections import defaultdict
import time

SYN_THRESHOLD = 20
PORTSCAN_THRESHOLD = 15
TIME_WINDOW = 10

syn_count = defaultdict(int)
scan_tracker = defaultdict(set)
last_seen = defaultdict(float)

def alert(msg):
    print("\n" + "=" * 50)
    print("[ALERT]", msg)
    print("=" * 50 + "\n")

def detect(pkt):
    if pkt.haslayer(IP) and pkt.haslayer(TCP):
        src_ip = pkt[IP].src
        dst_ip = pkt[IP].dst
        dst_port = pkt[TCP].dport
        flags = pkt[TCP].flags
        current_time = time.time()
        if current_time - last_seen[src_ip] > TIME_WINDOW:
            syn_count[src_ip] = 0
            scan_tracker[src_ip].clear()
        last_seen[src_ip] = current_time
        if flags == "S":
            syn_count[src_ip] += 1
            print(f"[SYN] {src_ip} -> {dst_ip}:{dst_port}")
            print(f"Count: {syn_count[src_ip]}")
            if syn_count[src_ip] > SYN_THRESHOLD:
                alert(f"Possible SYN Flood Attack from {src_ip}")
        scan_tracker[src_ip].add(dst_port)
        if len(scan_tracker[src_ip]) > PORTSCAN_THRESHOLD:
            alert(f"Possible Port Scan from {src_ip}")

print("\nMini IDS Started...")
print("Monitoring Network Traffic...\n")
sniff(prn=detect, store=0)
