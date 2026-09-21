class Vehicle:
    def __init__(self, number, model, rate):
        self.number = number
        self.model = model
        self.rate = rate
        self.available = True

    def rent(self):
        if self.available:
            self.available = False
            print("Vehicle rented")
        else:
            print("Vehicle not available")

    def return_vehicle(self, days):
        self.available = True
        print("Vehicle returned")
        print("Rental Charges:", self.rate * days)


v = Vehicle("MH12AB1234", "Swift", 1000)

v.rent()
v.return_vehicle(3)
