import pandas as pd

def validate_data(file_path: str) -> dict:
    """
    Validates the data for:
    - Null values per column
    - Duplicate patient IDs
    - Non-numeric ages

    Returns a dictionary with validation results.
    """
    df = pd.read_csv(file_path)
    results = {}

    # 1. Null Check
    nulls = df.isnull().sum()
    results["nulls"] = nulls[nulls > 0].to_dict()

    # 2. Duplicate PATIENT_IDs
    duplicates = df.duplicated(subset=["PATIENT_ID"]).sum()
    results["duplicates"] = int(duplicates)

    # 3. Invalid Age Values (not numeric or negative)
    if "AGE" in df.columns:
        non_numeric = df[~df["AGE"].apply(lambda x: str(x).isdigit())]
        results["invalid_ages"] = len(non_numeric)

    return results
