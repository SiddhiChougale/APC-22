
from database import get_connection
from menu import menu

connection = get_connection()
cursor = connection.cursor()

query = """
INSERT INTO menu_items
(item_id, category, item_name, price)
VALUES (%s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
category = VALUES(category),
item_name = VALUES(item_name),
price = VALUES(price)
"""

for item_id, item in menu.items():
    category, name, price = item

    cursor.execute(
        query,
        (item_id, category, name, price)
    )

connection.commit()

cursor.close()
connection.close()

print("Menu items saved in MySQL successfully!")
