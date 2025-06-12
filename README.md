# 📦 PII Masker
A lightweight Python tool for masking personally identifiable information (PII) in Excel, CSV, JSON, and log files. Designed for secure data sharing and privacy compliance.

## 🔐 Features
✅ Supports Excel (.xlsx, .xls), CSV, JSON, and .log (NDJSON) input files

✅ Masks names, email addresses (while preserving format), phone numbers, addresses, and organization names

✅ Maintains uniqueness across records using incremental labels (e.g., John Doe1, Company A)

✅ Automatically creates an output/ folder for masked files

✅ Command-line interface for easy automation

✅ Designed for use in audits, data sharing, and compliance workflows

## ⚙️ Usage
```bash
# Install dependencies
pip install -r requirements.txt

# Run the masker
python main.py path/to/input_file.xlsx "Test Company A"

```
The obfuscated file will be saved to:
```bash
output/input_file_masked.xlsx
```

## 📁 Example Input Columns Masked
- `First Name`, `Last Name`, `Full Name`, `Title`, `Email`, `Phone`, `Address`, `City`, `State`, `Zip`, `Country`, `Region`

- `Reader Company`, `Reader Org`, `Client` → Set to "Pace Lab" by default

