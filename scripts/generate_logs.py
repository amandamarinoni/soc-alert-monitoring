# scripts/generate_logs.py
import random
import os
from datetime import datetime, timedelta

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOG_DIR = os.path.join(BASE_DIR, "logs")
OUT_FILE = os.path.join(LOG_DIR, "generated_logs.log")
os.makedirs(LOG_DIR, exist_ok=True)

hosts = ["10.0.0.5", "10.0.0.12", "192.168.1.20", "203.0.113.50", "198.51.100.23"]
users = ["alice", "bob", "carol", "dave", "eve"]
apache_paths = ["/", "/login", "/admin", "/api/data", "/wp-login.php"]


def gen_ssh_line(dt, host, user, status):
    return (
        f"{dt} {host} sshd[{random.randint(1000, 9000)}]: {status} for {user} "
        f"from {host} port {random.randint(1024, 65000)}"
    )


def gen_apache_line(dt, ip, method, path, code, size):
    return f'{ip} - - [{dt}] "{method} {path} HTTP/1.1" {code} {size}'


def gen_windows_event(dt, host, user, event):
    return f"{dt} {host} EventID={random.choice([4625,4624,4672])} User={user} Msg={event}"


def random_date(start, end):
    delta = end - start
    sec = random.randint(0, int(delta.total_seconds()))
    return start + timedelta(seconds=sec)


def main():
    now = datetime.utcnow()
    start = now - timedelta(hours=2)
    lines = []

    for _ in range(1000):
        dt = random_date(start, now).strftime("%Y-%m-%dT%H:%M:%SZ")
        choice = random.random()

        if choice < 0.5:
            ip = random.choice(hosts)
            user = random.choice(users)
            status = random.choice(["Failed password", "Accepted password"])
            lines.append(gen_ssh_line(dt, ip, user, status))
        elif choice < 0.85:
            ip = random.choice(hosts)
            method = random.choice(["GET", "POST"])
            path = random.choice(apache_paths)
            code = random.choice([200, 200, 301, 404, 403, 500])
            size = random.randint(100, 5000)
            lines.append(gen_apache_line(dt, ip, method, path, code, size))
        else:
            ip = random.choice(hosts)
            user = random.choice(users)
            event = random.choice(["Logon Failure", "Logon Success", "Privilege Assigned"])
            lines.append(gen_windows_event(dt, ip, user, event))

    suspicious_ip = "203.0.113.99"
    bf_time = now - timedelta(minutes=30)
    for i in range(20):
        dt = (bf_time + timedelta(seconds=i * 5)).strftime("%Y-%m-%dT%H:%M:%SZ")
        lines.append(gen_ssh_line(dt, suspicious_ip, random.choice(users), "Failed password"))

    random.shuffle(lines)

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    print(f"[+] Generated {len(lines)} log lines at {OUT_FILE}")


if __name__ == "__main__":
    main()
