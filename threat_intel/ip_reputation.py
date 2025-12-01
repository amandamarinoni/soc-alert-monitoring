# threat_intel/ip_reputation.py
THREAT_DB = {
    "203.0.113.99": {"score": 95, "category": "malicious", "details": "Known brute-force source"},
    "198.51.100.23": {"score": 70, "category": "suspicious", "details": "Unusual traffic volume"},
    "192.168.1.20": {"score": 20, "category": "safe", "details": "Internal IP"},
    "10.0.0.5": {"score": 10, "category": "safe", "details": "Internal IP"},
}

DEFAULT_REPUTATION = {"score": 0, "category": "unknown", "details": "No records"}


def enrich_ip(ip: str):
    return THREAT_DB.get(ip, DEFAULT_REPUTATION)
