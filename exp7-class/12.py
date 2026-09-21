class FoodOrder:
    def __init__(self, order_id, name, food, quantity, price):
        self.order_id = order_id
        self.name = name
        self.food = food
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        total = self.quantity * self.price
        tax = total * 0.05
        return total + tax

    def __del__(self):
        print("Order completed")


order = FoodOrder(101, "Rahul", "Pizza", 2, 200)

print("Order ID:", order.order_id)
print("Customer:", order.name)
print("Food:", order.food)
print("Total Bill:", order.total_bill())
