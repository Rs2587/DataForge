import pandas as pd


def extract_data(file_path):
    df = pd.read_csv(file_path)

    print("Data extracted successfully.")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    return df