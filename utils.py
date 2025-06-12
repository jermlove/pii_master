import pandas as pd
import json

def load_input_file(path):
    if path.endswith(".csv"):
        return pd.read_csv(path)
    elif path.endswith(".xlsx") or path.endswith(".xls"):
        return pd.read_excel(path)
    elif path.endswith(".json"):
        with open(path, 'r', encoding='utf-8') as f:
            try:
                return pd.read_json(f)
            except ValueError:
                f.seek(0)
                return pd.DataFrame([json.loads(line) for line in f if line.strip()])
    elif path.endswith(".log"):
        with open(path, 'r', encoding='utf-8') as f:
            return pd.DataFrame([json.loads(line) for line in f if line.strip()])
    else:
        raise ValueError("Unsupported file type. Please provide a CSV, Excel, JSON, or log file.")

def save_output_file(df, output_path):
    df.to_excel(output_path, index=False)