from masking import mask_pii_data
from utils import load_input_file, save_output_file
import sys
import os

def main(input_path):
    if not os.path.isfile(input_path):
        print(f"File not found: {input_path}")
        return

    print(f"Loading file: {input_path}")
    df = load_input_file(input_path)

    print("Masking PII fields...")
    masked_df = mask_pii_data(df)

    # Create output directory if not exists
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(output_dir, f"{base_name}_masked.xlsx")

    save_output_file(masked_df, output_path)
    print(f"Masked file saved to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file.xlsx|.csv>")
    else:
        main(sys.argv[1])