import yaml
import pandas as pd
from agents.watcher import detect_schema_drift
from agents.validator import validate_data
from agents.fixer import suggest_fixes
from agents.notifier import notify

def main():
    # Load config file
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

    v1_path = config["baseline_file"]
    v2_path = config["target_file"]

    print(">> Running Watcher Agent...")
    drift = detect_schema_drift(v1_path, v2_path)
    print("Schema Drift Detected:", drift)

    print("\n>> Running Validator Agent...")
    validation_results = validate_data(v2_path)
    print("Validation Results:", validation_results)

    print("\n>> Running Fixer Agent...")
    fix_code = suggest_fixes(validation_results)
    print("Suggested Fix:\n")
    print(fix_code)

    with open("logs/suggested_fix.txt", "w") as f:
        f.write("```python\n")
        f.write(fix_code)
        f.write("\n```")

    # Notifier (e.g., log to console, email, or file)
    print("\n>> Generating Report via Notifier Agent...")
    notify({
        "drift": drift,
        "validation": validation_results,
        "fix_code": fix_code,
    })

if __name__ == "__main__":
    main()
