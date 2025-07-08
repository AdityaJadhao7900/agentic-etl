import pandas as pd

def detect_schema_drift(old_file: str, new_file: str) -> list[str]:
    df_old = pd.read_csv(old_file)
    df_new = pd.read_csv(new_file)

    drift = list(set(df_new.columns) - set(df_old.columns))
    return drift
