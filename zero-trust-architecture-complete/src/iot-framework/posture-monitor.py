import json

def audit(device):
    issues = []
    if not device.get("firmware_up_to_date"): issues.append("Firmware outdated")
    if not device.get("tls_enabled"): issues.append("TLS not enabled")
    return {"device": device["id"], "issues": issues} if issues else None

def main():
    with open("iot_devices.json") as f:
        devices = json.load(f)
    results = [audit(d) for d in devices if audit(d)]
    with open("iot_audit_report.json", "w") as f: json.dump(results, f, indent=2)

if __name__ == '__main__':
    main()
