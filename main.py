from masking import mask_pii_data
from utils import load_input_file, save_output_file
import sys
import os

def main(input_path, client_name):
    if not os.path.isfile(input_path):
        print(f"File not found: {input_path}")
        return

    print(f"Loading file: {input_path}")
    df = load_input_file(input_path)

    print(f"Masking PII fields with client: {client_name}")
    masked_df = mask_pii_data(df, client_name=client_name)

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    base_name, ext = os.path.splitext(os.path.basename(input_path))
    output_path = os.path.join(output_dir, f"{base_name}_masked{ext}")

    save_output_file(masked_df, output_path)
    print(f"Masked file saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <input_file> <client_name>")
    else:
        main(sys.argv[1], sys.argv[2])
