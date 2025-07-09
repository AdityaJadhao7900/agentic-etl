🧠 Agentic Data Fixer

A local LLM-powered agentic pipeline to detect, validate, and suggest fixes for schema drift and data quality issues in your CSV data — autonomously.

No OpenAI. No cloud APIs. Entirely local. Built using Ollama and deepseek-coder:6.7b.

🚀 What It Does

Given two versions of a dataset:

✅ Watcher Agent detects schema drift between versions

✅ Validator Agent checks for data issues: nulls, duplicates, invalid values

✅ Fixer Agent (powered by LLM) suggests pandas code to clean the data

✅ Notifier Agent logs a Markdown report and stores the fix

This is designed to run fully offline with Ollama and can be adapted to monitor Delta tables or Azure Blob Storage.


🛠️ Setup Instructions

On macOS/Linux

# Install Ollama
brew install ollama
ollama pull deepseek-coder:6.7b

# Clone and setup
git clone https://github.com/your-handle/agentic-etl.git
cd agentic-etl
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Update config.yaml with your file paths

# Run it
python main.py

On Windows

# Install Ollama for Windows
Download and install from https://ollama.com/download
Open Command Prompt or PowerShell:
ollama pull deepseek-coder:6.7b

# Clone and setup
cd your/project/directory
git clone https://github.com/your-handle/agentic-etl.git
cd agentic-etl
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Update config.yaml with your file paths

# Run it
python main.py

💡 Example Output

>> Running Watcher Agent...
Schema Drift Detected: ['RACE_DESC']

>> Running Validator Agent...
Validation Results: {'nulls': {'AGE': 2}, 'duplicates': 1, 'invalid_ages': 3}

>> Running Fixer Agent...
Suggested Fix:

def fix_data(df: pd.DataFrame) -> pd.DataFrame:
    ...

>> Generating Report via Notifier Agent...
✅ Logs saved to logs/report.md and logs/suggested_fix.txt

📈 Next Steps

Add Blob Storage / Delta Table support for Fabric

Let the Fixer Agent automatically apply fixes

Build a dashboard for real-time agent runs

👨‍💻 Built With

Python 3.11

Pandas, PyYAML

Ollama (DeepSeek)

Modular agent-based architecture



Connect with me on [LinkedIn](https://www.linkedin.com/in/aditya-j-3651521a4/).

⚠️ Disclaimer

This is an experimental local agent framework for learning and prototyping. Always test the fix logic before applying it to critical systems.

