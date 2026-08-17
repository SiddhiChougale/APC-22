# Visitors on two different days
day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 105, 106, 107}

# Unique visitors across both days
unique_visitors = day1 | day2

# Returning visitors
returning_visitors = day1 & day2

# Visitors only on first day
first_day_only = day1 - day2

# Visitors only on second day
second_day_only = day2 - day1

print("Unique visitors:", unique_visitors)
print("Returning visitors:", returning_visitors)
print("First day only:", first_day_only)
print("Second day only:", second_day_only)


# Products in two different categories
electronics = {"Laptop", "Phone", "Tablet", "Camera"}
gadgets = {"Phone", "Tablet", "Smartwatch", "Headphones"}

# Products belonging to both categories
common_products = electronics & gadgets

print("Products in both categories:", common_products)
