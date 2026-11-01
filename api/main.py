import os
from datetime import datetime

import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


# -----------------------------------
# Load Environment Variables
# -----------------------------------

load_dotenv()


# -----------------------------------
# FastAPI Application
# -----------------------------------

app = FastAPI(
    title="DataForge API",
    description="REST API for the DataForge data pipeline",
    version="1.0.0"
)


# -----------------------------------
# Customer Response Model
# -----------------------------------

class Customer(BaseModel):
    customer_id: int
    name: str
    email: str
    city: str
    age: int
    purchase_amount: float
    created_at: datetime | None = None


# -----------------------------------
# Database Connection
# -----------------------------------

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


# -----------------------------------
# Home Endpoint
# -----------------------------------

@app.get("/")
def home():
    return {
        "message": "DataForge API is running"
    }


# -----------------------------------
# Get All Customers
# -----------------------------------

@app.get("/customers", response_model=list[Customer])
def get_customers():

    connection = None
    cursor = None

    try:
        connection = get_connection()

        cursor = connection.cursor(
            dictionary=True
        )

        cursor.execute(
            "SELECT * FROM customers"
        )

        customers = cursor.fetchall()

        return customers

    except Error:
        raise HTTPException(
            status_code=503,
            detail="Database service unavailable"
        )

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()


# -----------------------------------
# Get Customer By ID
# -----------------------------------

@app.get(
    "/customers/{customer_id}",
    response_model=Customer
)
def get_customer(customer_id: int):

    connection = None
    cursor = None

    try:

        connection = get_connection()

        cursor = connection.cursor(
            dictionary=True
        )

        query = """
            SELECT *
            FROM customers
            WHERE customer_id = %s
        """

        cursor.execute(
            query,
            (customer_id,)
        )

        customer = cursor.fetchone()

        if customer is None:
            raise HTTPException(
                status_code=404,
                detail="Customer not found"
            )

        return customer

    except HTTPException:
        raise

    except Error:
        raise HTTPException(
            status_code=503,
            detail="Database service unavailable"
        )

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()