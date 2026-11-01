import pandas as pd

from src.validate import validate_data


def test_valid_data():

    df = pd.DataFrame({
        "customer_id": [101, 102],
        "name": ["Rahul", "Neha"],
        "email": ["rahul@gmail.com", "neha@gmail.com"],
        "city": ["Pune", "Mumbai"],
        "age": [25, 29],
        "purchase_amount": [15000, 22000]
    })

    assert validate_data(df) is True


def test_negative_age_fails_validation():

    df = pd.DataFrame({
        "customer_id": [101],
        "name": ["Rahul"],
        "email": ["rahul@gmail.com"],
        "city": ["Pune"],
        "age": [-5],
        "purchase_amount": [15000]
    })

    assert validate_data(df) is False


def test_negative_purchase_amount_fails_validation():

    df = pd.DataFrame({
        "customer_id": [101],
        "name": ["Rahul"],
        "email": ["rahul@gmail.com"],
        "city": ["Pune"],
        "age": [25],
        "purchase_amount": [-100]
    })

    assert validate_data(df) is False