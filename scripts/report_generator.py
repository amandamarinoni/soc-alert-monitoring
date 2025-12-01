# scripts/report_generator.py
import json
from tabulate import tabulate
from datetime import datetime
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ALERTS = os.path.join(BASE_DIR, "logs", "alerts.json")
OUT = os.path.join(BASE_DIR, "logs", "incident_report.md")


def severity(a):
    t = a.get("type")
    if t == "brute_force":
        return "High"
    if t in ("suspicious_http", "high_activity"):
        return "Medium"
    return "Low"


def load_alerts():
    try:
        with open(ALERTS, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def generate():
    alerts = load_alerts()
    lines = []

    lines.append(f"# Incident Report\nGenerated: {datetime.utcnow().isoformat()}Z\n")

    if not alerts:
        lines.append("No alerts detected.\n")
    else:
        table = []
        for i, a in enumerate(alerts, 1):
            rep = a.get("reputation", {})
            notes = a.get("description") or a.get("raw", "")
            table.append(
                [
                    i,
                    a.get("type"),
                    a.get("ip", "-"),
                    severity(a),
                    rep.get("category", "unknown"),
                    rep.get("score", 0),
                    notes,
                ]
            )

        lines.append("## Summary\n")
        lines.append(
            tabulate(
                table,
                headers=["#", "Type", "IP", "Severity", "Rep Category", "Rep Score", "Notes"],
                tablefmt="github",
            )
        )
        lines.append("\n")

        lines.append("## Details\n")
        for i, a in enumerate(alerts, 1):
            lines.append(f"### Alert {i}: {a.get('type')}")
            for k, v in a.items():
                if k == "reputation":
                    lines.append(f"- **reputation.score**: {v.get('score')}")
                    lines.append(f"- **reputation.category**: {v.get('category')}")
                    lines.append(f"- **reputation.details**: {v.get('details')}")
                else:
                    lines.append(f"- **{k}**: {v}")
            lines.append("")

    lines.append("## Playbook\n")
    lines.append("- Isolar IP suspeito")
    lines.append("- Resetar credenciais afetadas")
    lines.append("- Coletar evidências e consolidar logs")
    lines.append("- Notificar equipe N2/SecOps")
    lines.append("- Revisar políticas de segurança\n")

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[+] Report saved to {OUT}")


if __name__ == "__main__":
    generate()
