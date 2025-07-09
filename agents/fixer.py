import requests

def suggest_fixes(validation_results: str) -> str:
    """Uses local Ollama model (deepseek-coder:6.7b) to suggest code fixes."""
    payload = {
        "model": "deepseek-coder:6.7b",
        "prompt": f"""You are a senior data engineer. You are given the following validation results from a Pandas DataFrame:
        {validation_results}

        Suggest a Python pandas code block that can fix these issues safely and log them.
        Don't include import statements.
        Just return code inside a function called `fix_data(df: pd.DataFrame) -> pd.DataFrame`.
        Make sure it does not fail if a column is missing.
        """,
        "stream": False
    }

    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        response.raise_for_status()
        return response.json()["response"]
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to connect to Ollama: {e}")
