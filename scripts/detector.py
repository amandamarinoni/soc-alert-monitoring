import re
import json
from collections import defaultdict, deque
from datetime import datetime, timedelta
import os

LOGFILE = "../logs/generated_logs.log"
BRUTE_FORCE_THRESHOLD = 10
BRUTE_WINDOW_SECONDS = 60
ACTIVE_IP_THRESHOLD = 50
SUSPICIOUS_PATHS = ["/wp-login.php", "/admin", "/login", "/phpmyadmin"]

ssh_re = re.compile(r'(?P<ts>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)\s+(?P<ip>[\d\.]+)\s+sshd\[\d+\]:\s+(?P<status>Failed password|Accepted password)\s+for\s+(?P<user>\w+)\s+from\s+(?P<fromip>[\d\.]+)')
apache_re = re.compile(r'(?P<ip>[\d\.]+)\s+- - \[(?P<ts>[^\]]+)\]\s+"(?P<method>GET|POST)\s+(?P<path>\S+)\s+HTTP/1\.\d"\s+(?P<code>\d{3})\s+(?P<size>\d+)')
windows_re = re.compile(r'(?P<ts>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)\s+(?P<host>[\d\.]+)\s+EventID=(?P<id>\d+)\s+User=(?P<user>\w+)\s+Msg=(?P<msg>.+)')

def parse_ts(ts_str):
    try:
        return datetime.strptime(ts_str, "%Y-%m-%dT%H:%M:%SZ")
    except:
        return None

def detect():
    ip_event_count = defaultdict(int)
    ip_failed_queue = defaultdict(lambda: deque())
    alerts = []

    if not os.path.exists(LOGFILE):
        print("[!] Missing log file. Run generate_logs.py first.")
        return

    with open(LOGFILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            # SSH
            m = ssh_re.search(line)
            if m:
                ts = parse_ts(m.group("ts"))
                ip = m.group("fromip")
                status = m.group("status")
                user = m.group("user")
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
                            "description": f"{len(q)} failed SSH attempts detected"
                        })
                        q.clear()
                continue

            # Apache
            m = apache_re.search(line)
            if m:
                ip = m.group("ip")
                path = m.group("path")
                code = int(m.group("code"))
                ip_event_count[ip] += 1

                if path in SUSPICIOUS_PATHS or code in (401,403,500):
                    alerts.append({
                        "type": "suspicious_http",
                        "ip": ip,
                        "path": path,
                        "code": code,
                        "raw": line
                    })
                continue

            # Windows
            m = windows_re.search(line)
            if m:
                ip = m.group("host")
                user = m.group("user")
                msg = m.group("msg")
                ip_event_count[ip] += 1

                if "failure" in msg.lower():
                    alerts.append({
                        "type": "windows_logon_failure",
                        "ip": ip,
                        "user": user,
                        "msg": msg
                    })
                continue

    for ip, count in ip_event_count.items():
        if count >= ACTIVE_IP_THRESHOLD:
            alerts.append({
                "type": "high_activity",
                "ip": ip,
                "count": count,
                "description": f"IP {ip} generated {count} events"
            })

    os.makedirs("../logs", exist_ok=True)
    out = "../logs/alerts.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(alerts, f, indent=2)

    print(f"[+] Detection complete. Alerts saved to {out}")

if __name__ == "__main__":
    detect()
