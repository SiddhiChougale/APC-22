class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand:", self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        Vehicle.__init__(self, brand)
        self.model = model

    def car_info(self):
        print("Model:", self.model)


class Bike(Vehicle):
    def __init__(self, brand, model):
        Vehicle.__init__(self, brand)
        self.model = model

    def bike_info(self):
        print("Model:", self.model)


class SportsCar(Car):
    def __init__(self, brand, model, speed):
        Car.__init__(self, brand, model)
        self.speed = speed

    def display_sports_car(self):
        self.display()
        self.car_info()
        print("Top Speed:", self.speed, "km/h")


class ElectricBike(Bike):
    def __init__(self, brand, model, battery):
        Bike.__init__(self, brand, model)
        self.battery = battery

    def display_electric_bike(self):
        self.display()
        self.bike_info()
        print("Battery:", self.battery, "kWh")


S = SportsCar("Ferrari", "488", 330)
E = ElectricBike("Ather", "450X", 3.7)

S.display_sports_car()
print("----")
E.display_electric_bike()
