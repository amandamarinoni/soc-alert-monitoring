# scripts/detector.py
import re
import json
import os
from collections import defaultdict, deque
from datetime import datetime, timezone

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOG_FILE = os.path.join(BASE_DIR, "logs", "generated_logs.log")
OUT_FILE = os.path.join(BASE_DIR, "logs", "alerts.json")
os.makedirs(os.path.join(BASE_DIR, "logs"), exist_ok=True)

BRUTE_FORCE_THRESHOLD = 10
BRUTE_WINDOW_SECONDS = 60
ACTIVE_IP_THRESHOLD = 50
SUSPICIOUS_PATHS = ["/wp-login.php", "/admin", "/login", "/phpmyadmin"]

ssh_re = re.compile(
    r'(?P<ts>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)\s+(?P<host>[\d\.]+)\s+sshd\[\d+\]:\s+'
    r'(?P<status>Failed password|Accepted password)\s+for\s+(?P<user>\w+)\s+from\s+'
    r'(?P<fromip>[\d\.]+)'
)
apache_re = re.compile(
    r'(?P<ip>[\d\.]+)\s+- - \[(?P<ts>[^\]]+)\]\s+"(?P<method>GET|POST)\s+'
    r'(?P<path>\S+)\s+HTTP/1\.\d"\s+(?P<code>\d{3})\s+(?P<size>\d+)'
)
windows_re = re.compile(
    r'(?P<ts>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)\s+'
    r'(?P<host>[\d\.]+)\s+EventID=(?P<id>\d+)\s+User=(?P<user>\w+)\s+Msg=(?P<msg>.+)'
)

try:
    from threat_intel.ip_reputation import enrich_ip  # type: ignore
except Exception:
    def enrich_ip(ip: str):
        return {"score": 0, "category": "unknown", "details": "No local threat intel available"}


def parse_ts_iso_z(ts_str: str):
    try:
        return datetime.strptime(ts_str, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except Exception:
        return None


def detect():
    if not os.path.exists(LOG_FILE):
        print(f"[!] Log file not found at: {LOG_FILE}")
        print("[!] Run generate_logs.py first.")
        return []

    event_count = defaultdict(int)
    failed_queue = defaultdict(lambda: deque())
    alerts = []

    with open(LOG_FILE, "r", encoding="utf-8") as fh:
        lines = fh.readlines()

    for raw in lines:
        line = raw.strip()
        if not line:
            continue

        m = ssh_re.search(line)
        if m:
            ts = parse_ts_iso_z(m.group("ts"))
            source_ip = m.group("fromip")
            status = m.group("status")

            event_count[source_ip] += 1

            if status == "Failed password":
                q = failed_queue[source_ip]
                ts_use = ts or datetime.now(timezone.utc)
                q.append(ts_use)
                while q and (ts_use - q[0]).total_seconds() > BRUTE_WINDOW_SECONDS:
                    q.popleft()
                if len(q) >= BRUTE_FORCE_THRESHOLD:
                    rep = enrich_ip(source_ip)
                    alerts.append(
                        {
                            "type": "brute_force",
                            "ip": source_ip,
                            "count_in_window": len(q),
                            "first_detected": q[0].astimezone(timezone.utc).isoformat(),
                            "last_detected": q[-1].astimezone(timezone.utc).isoformat(),
                            "description": f"SSH brute force detected: {len(q)} failed attempts",
                            "reputation": rep,
                        }
                    )
                    q.clear()
            continue

        m = apache_re.search(line)
        if m:
            ip = m.group("ip")
            path = m.group("path")
            code = int(m.group("code"))
            event_count[ip] += 1

            if path in SUSPICIOUS_PATHS or code in (401, 403, 500):
                rep = enrich_ip(ip)
                alerts.append(
                    {
                        "type": "suspicious_http",
                        "ip": ip,
                        "path": path,
                        "code": code,
                        "description": f"Suspicious HTTP activity on {path} ({code})",
                        "reputation": rep,
                    }
                )
            continue

        m = windows_re.search(line)
        if m:
            host = m.group("host")
            msg = m.group("msg")
            event_count[host] += 1

            if "failure" in msg.lower() or "logon failure" in msg.lower():
                rep = enrich_ip(host)
                alerts.append(
                    {
                        "type": "windows_logon_failure",
                        "ip": host,
                        "msg": msg,
                        "description": f"Windows logon failure: {msg}",
                        "reputation": rep,
                    }
                )
            continue

        other_ip_match = re.match(r"^(?P<ip>[\d\.]+)\s", line)
        if other_ip_match:
            ip = other_ip_match.group("ip")
            event_count[ip] += 1

    for ip, count in event_count.items():
        if count >= ACTIVE_IP_THRESHOLD:
            rep = enrich_ip(ip)
            alerts.append(
                {
                    "type": "high_activity",
                    "ip": ip,
                    "count": count,
                    "description": f"IP {ip} generated {count} events (threshold {ACTIVE_IP_THRESHOLD})",
                    "reputation": rep,
                }
            )

    try:
        with open(OUT_FILE, "w", encoding="utf-8") as outf:
            json.dump(alerts, outf, indent=2, ensure_ascii=False)
        print(f"[+] Detection complete. Alerts saved to {OUT_FILE} ({len(alerts)} alerts).")
    except Exception as exc:
        print(f"[!] Failed to write alerts file: {exc}")

    return alerts


if __name__ == "__main__":
    detect()
