cart = []

# Add item
cart.append("Apple")
cart.append("Milk")
cart.append("Bread")

# Display cart
print("Cart:", cart)

# Search item
item = input("Enter item to search: ")

if item in cart:
    print("Item found")
else:
    print("Item not found")

# Remove item
item = input("Enter item to remove: ")

if item in cart:
    cart.remove(item)
    print("Item removed")
else:
    print("Item not found")

# Display updated cart
print("Updated cart:", cart)

# Count total items
print("Total items:", len(cart))