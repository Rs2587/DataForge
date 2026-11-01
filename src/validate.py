import pandas as pd


def validate_data(df):
    """
    Validate transformed customer data.
    """

    errors = []

    # 1. Check customer_id
    if df["customer_id"].isnull().any():
        errors.append("customer_id contains missing values.")

    if df["customer_id"].duplicated().any():
        errors.append("Duplicate customer_id found.")

    # 2. Check name
    if df["name"].isnull().any():
        errors.append("name contains missing values.")

    # 3. Check email
    if df["email"].isnull().any():
        errors.append("email contains missing values.")

    # 4. Check age
    if (df["age"] < 0).any():
        errors.append("age contains negative values.")

    # 5. Check purchase amount
    if (df["purchase_amount"] < 0).any():
        errors.append("purchase_amount contains negative values.")

    # Final result
    if errors:
        print("\n❌ Data validation failed.")

        for error in errors:
            print(f"- {error}")

        return False

    print("\n✅ Data validation successful.")

    return True