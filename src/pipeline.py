from src.extract import extract_data
from src.transform import transform_data
from src.validate import validate_data
from src.load import load_data


FILE_PATH = "data/raw/customers.csv"


if __name__ == "__main__":

    # Extract
    df = extract_data(FILE_PATH)

    # Transform
    df = transform_data(df)

    # Validate
    is_valid = validate_data(df)

    # Load
    if is_valid:
        load_data(df)
    else:
        print("❌ Pipeline stopped because validation failed.")