import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-alpha"
HEADERS = {
    "Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}",
    "Content-Type": "application/json"
}

def suggest_fixes(validation_results: dict) -> str:
    prompt = f"""
You are a senior data engineer. You are given validation issues from a dataset:
{json.dumps(validation_results, indent=2)}

Suggest a Python pandas code block that can fix these issues safely and log them.
Don't include import statements.
Just code inside a function called `fix_data(df: pd.DataFrame) -> pd.DataFrame`.
Make sure it doesn't fail if columns are missing.
    """

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 512,
            "temperature": 0.5,
            "do_sample": True,
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()
    return response.json()[0]["generated_text"].strip()
