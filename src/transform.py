import pandas as pd

from src.transform import transform_data


def test_transform_removes_duplicate_customer_ids():

    df = pd.DataFrame({
        "customer_id": [101, 102, 102],
        "name": [" Rahul Patil ", "Neha Sharma", "Neha Sharma"],
        "email": ["rahul@gmail.com", "neha@gmail.com", "neha@gmail.com"],
        "city": ["Pune", "mumbai", "mumbai"],
        "age": [25, 29, 29],
        "purchase_amount": [15000, 22000, 22000]
    })

    result = transform_data(df)

    assert len(result) == 2
    assert result["customer_id"].is_unique


def test_transform_cleans_name_and_city():

    df = pd.DataFrame({
        "customer_id": [101],
        "name": ["   Rahul Patil   "],
        "email": ["rahul@gmail.com"],
        "city": ["mumbai"],
        "age": [25],
        "purchase_amount": [15000]
    })

    result = transform_data(df)

    assert result.iloc[0]["name"] == "Rahul Patil"
    assert result.iloc[0]["city"] == "Mumbai"


def test_transform_fills_missing_values():

    df = pd.DataFrame({
        "customer_id": [101, 102],
        "name": ["Rahul", "Neha"],
        "email": ["rahul@gmail.com", None],
        "city": ["Pune", "Mumbai"],
        "age": [25, None],
        "purchase_amount": [15000, 22000]
    })

    result = transform_data(df)

    assert result["email"].isnull().sum() == 0
    assert result["age"].isnull().sum() == 0