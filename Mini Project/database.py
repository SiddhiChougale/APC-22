
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    return connection

def get_menu_items():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT item_id, category, item_name, price "
        "FROM menu_items ORDER BY item_id"
    )

    items = cursor.fetchall()

    cursor.close()
    connection.close()

    return items


def save_order(orders, subtotal, gst, grand_total):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Save the main bill
        cursor.execute(
            """
            INSERT INTO orders (subtotal, gst, grand_total)
            VALUES (%s, %s, %s)
            """,
            (subtotal, gst, grand_total)
        )

        # Get the new Order ID
        order_id = cursor.lastrowid

        # Save each food item in this order
        for order in orders:
            name, price, quantity, total = order

            cursor.execute(
                """
                INSERT INTO order_items
                (order_id, item_name, price, quantity, total)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (order_id, name, price, quantity, total)
            )

        connection.commit()
        return order_id

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()
