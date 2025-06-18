import json, os

def check_mfa(users):
    return [f"User {u['username']} missing MFA" for u in users if not u.get("mfa_enabled")]

def run_scan(input_file, output_file):
    with open(input_file) as f: users = json.load(f)
    report = {"mfa_issues": check_mfa(users)}
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as f: json.dump(report, f, indent=2)

if __name__ == "__main__":
    run_scan("sample_users.json", "output/compliance_report.json")
