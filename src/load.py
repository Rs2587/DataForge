import os

import mysql.connector
from dotenv import load_dotenv


load_dotenv()


def load_data(df):

    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME", "dataforge")
    )

    cursor = connection.cursor()

    query = """
        INSERT INTO customers
        (
            customer_id,
            name,
            email,
            city,
            age,
            purchase_amount
        )
        VALUES (%s, %s, %s, %s, %s, %s)

        ON DUPLICATE KEY UPDATE
            name = VALUES(name),
            email = VALUES(email),
            city = VALUES(city),
            age = VALUES(age),
            purchase_amount = VALUES(purchase_amount)
    """

    for _, row in df.iterrows():

        values = (
            int(row["customer_id"]),
            row["name"],
            row["email"],
            row["city"],
            int(row["age"]),
            float(row["purchase_amount"])
        )

        cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

    print("✅ Data loaded successfully into MySQL.")