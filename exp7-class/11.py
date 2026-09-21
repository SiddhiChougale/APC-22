class ShoppingCart:
    def __init__(self, name, cart_id):
        self.name = name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, product, price):
        self.products.append((product, price))

    def remove_product(self, product):
        for p in self.products:
            if p[0] == product:
                self.products.remove(p)

    def total_bill(self):
        total = 0
        for p in self.products:
            total += p[1]
        return total

    def __del__(self):
        print("Shopping cart destroyed")


cart = ShoppingCart("Rahul", 101)

cart.add_product("Pen", 20)
cart.add_product("Book", 100)

print("Total Bill:", cart.total_bill())

cart.remove_product("Pen")
print("Total Bill after removal:", cart.total_bill())
