import re
import json
from collections import defaultdict, deque
from datetime import datetime, timedelta
import os

# Caminho absoluto da raiz do projeto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOG_FILE = os.path.join(BASE_DIR, "logs", "generated_logs.log")
OUT_FILE = os.path.join(BASE_DIR, "logs", "alerts.json")

# Garante que a pasta logs existe
os.makedirs(os.path.join(BASE_DIR, "logs"), exist_ok=True)

BRUTE_FORCE_THRESHOLD = 10
BRUTE_WINDOW_SECONDS = 60
ACTIVE_IP_THRESHOLD = 50
SUSPICIOUS_PATHS = ["/wp-login.php", "/admin", "/login", "/phpmyadmin"]

ssh_re = re.compile(
    r'(?P<ts>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)\s+(?P<ip>[\d\.]+)\s+sshd\[\d+\]:\s+(?P<status>Failed password|Accepted password)\s+for\s+(?P<user>\w+)\s+from\s+(?P<fromip>[\d\.]+)'
)

apache_re = re.compile(
    r'(?P<ip>[\d\.]+)\s+- - \[(?P<ts>[^\]]+)\]\s+"(?P<method>GET|POST)\s+(?P<path>\S+)\s+HTTP/1\.\d"\s+(?P<code>\d{3})\s+(?P<size>\d+)'
)

windows_re = re.compile(
    r'(?P<ts>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)\s+(?P<host>[\d\.]+)\s+EventID=(?P<id>\d+)\s+User=(?P<user>\w+)\s+Msg=(?P<msg>.+)'
)

def parse_ts(ts_str):
    try:
        return datetime.strptime(ts_str, "%Y-%m-%dT%H:%M:%SZ")
    except:
        return None

def detect():
    if not os.path.exists(LOG_FILE):
        print(f"[!] Log file not found at: {LOG_FILE}")
        print("[!] Run generate_logs.py first.")
        return

    ip_event_count = defaultdict(int)
    ip_failed_queue = defaultdict(lambda: deque())
    alerts = []

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()

        # ---------------- SSH ----------------
        m = ssh_re.search(line)
        if m:
            ts = parse_ts(m.group("ts"))
            ip = m.group("fromip")
            status = m.group("status")
            ip_event_count[ip] += 1

            if status == "Failed password":
                q = ip_failed_queue[ip]
                q.append(ts)

                while q and (ts - q[0]).total_seconds() > BRUTE_WINDOW_SECONDS:
                    q.popleft()

                if len(q) >= BRUTE_FORCE_THRESHOLD:
                    alerts.append({
                        "type": "brute_force",
                        "ip": ip,
                        "count_in_window": len(q),
                        "first_detected": q[0].isoformat() + "Z",
                        "last_detected": q[-1].isoformat() + "Z",
                        "description": f"SSH brute force detected: {len(q)} failed attempts"
                    })
                    q.clear()

            continue

        # -------------- Apache --------------
        m = apache_re.search(line)
        if m:
            ip = m.group("ip")
            path = m.group("path")
            code = int(m.group("code"))
            ip_event_count[ip] += 1

            if path in SUSPICIOUS_PATHS or code in (401, 403, 500):
                alerts.append({
                    "type": "suspicious_http",
                    "ip": ip,
                    "path": path,
                    "code": code,
                    "description": f"Suspicious HTTP activity on {path} ({code})"
                })
            continue

        # -------------- Windows --------------
        m = windows_re.search(line)
        if m:
            ip = m.group("host")
            msg = m.group("msg")
            ip_event_count[ip] += 1

            if "failure" in msg.lower():
                alerts.append({
                    "type": "windows_logon_failure",
                    "ip": ip,
                    "msg": msg,
                })
            continue

    # -------------- High Activity --------------
    for ip, count in ip_event_count.items():
        if count >= ACTIVE_IP_THRESHOLD:
            alerts.append({
                "type": "high_activity",
                "ip": ip,
                "count": count,
                "description": f"High activity detected from IP: {ip}"
            })

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(alerts, f, indent=2)

    print(f"[+] Detection complete. Alerts saved to {OUT_FILE}")

if __name__ == "__main__":
    detect()
