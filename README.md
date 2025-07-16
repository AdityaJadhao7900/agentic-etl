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

Here is the Python pandas code block that can handle these issues safely and log them in a dictionary.

```python
def fix_data(df):
    validation_results = {}  # Initialize an empty dict for validation results
    
    if 'AGE' not in df.columns:
        return df, validation_results

    # Checking for nulls
    if df['AGE'].isnull().sum() > 0:
        df = df[df['AGE'].notna()]  # Remove rows with null ages
        validation_results['nulls'] = 1  

    # Checking for duplicates
    if df.duplicated(subset='AGE').sum() > 0:
        df = df.drop_duplicates(subset='AGE')  # Drop duplicate rows with the same age
        validation_results['duplicates'] = 1  
    
    # Checking for invalid ages (assuming ages less than 0 as invalid)
    if (df['AGE'] < 0).sum() > 0:
        df = df[df['AGE'] >= 0]  # Drop rows with negative or zero age
        validation_results['invalid_ages'] = 1  
    
    return df, validation_results
```
In this function, it first checks if the 'AGE' column is present in the DataFrame. If not, it returns the original DataFrame and an empty dictionary for validation results as there are no issues to fix. Then, it handles each issue separately:
- For nulls, it removes rows that contain null values in the 'AGE' column. 
- For duplicates, it drops duplicate rows based on the age. 
- Finally, for invalid ages (assuming those less than zero as invalid), it also removes these rows from the DataFrame.

It logs the number of issues handled by each step into a dictionary and returns this along with the modified DataFrame. It should be noted that if a column is missing in the original DataFrame, the function will return an identical DataFrame without any changes to it as no issues exist in such a case.


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

