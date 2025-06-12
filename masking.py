import pandas as pd

def generate_unique_mapping(series, base_label, suffix_format="{base}{num}"):
    unique_values = series.dropna().unique()
    mapping = {orig: suffix_format.format(base=base_label, num=i + 1) for i, orig in enumerate(unique_values)}
    return series.map(mapping)

def mask_pii_data(df):
    unique_fields = {
        'First Name': 'John',
        'Last Name': 'Doe',
        'Full Name': 'John Doe',
        'Title': 'Professional',
        'Reader Company': 'Company',
        'Reader Org': 'Org'
    }

    static_fields = {
        'Phone': '000-000-0000',
        'Address': '123 Main St',
        'City': 'Anytown',
        'State': 'ST',
        'Zip': '00000',
        'Country': 'CountryX',
        'Region': 'RegionX'
    }

    for col, base in unique_fields.items():
        if col in df.columns:
            df[col] = generate_unique_mapping(df[col], base)

    if 'Email' in df.columns:
        unique_emails = df['Email'].dropna().unique()
        email_mapping = {orig: f"user{i+1}@example.com" for i, orig in enumerate(unique_emails)}
        df['Email'] = df['Email'].map(email_mapping)

    for col, val in static_fields.items():
        if col in df.columns:
            df[col] = val

    if 'Client' in df.columns:
        df['Client'] = "Pace Lab"

    return df