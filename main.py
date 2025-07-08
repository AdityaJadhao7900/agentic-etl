from agents.watcher import detect_schema_drift
from agents.validator import validate_data
from agents.fixer import suggest_fixes

if __name__ == "__main__":
    print(">> Running Watcher Agent...")
    drift = detect_schema_drift("data/patient_data_v1.csv", "data/patient_data_v2.csv")
    print("Schema Drift Detected:", drift)

    print("\n>> Running Validator Agent...")
    validation_results = validate_data("data/patient_data_v2.csv")
    print("Validation Results:", validation_results)

    print("\n>> Running Fixer Agent...")
    fix_code = suggest_fixes(validation_results)
    print("Suggested Fix:\n")
    print(fix_code)
