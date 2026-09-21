class Vehicle:
    def  __init__(self,brand,model):
        self.brand=brand
        self.model=model 

    def display(self):
        print("Brand: ",self.brand)
        print("Model: ",self.model)


class Car(Vehicle):
    def __init__(self, brand, model,fule_type,price):
        super().__init__(brand, model)
        self.fule_type=fule_type
        self.price=price

    def display(self):
        super().display()
        print("Fule_type: ",self.fule_type)
        print("Price: ",self.price)
        print("-----")

C1=Car("TATA","CURVV","Deisel",1800000)
C2=Car("BMW","X5","Petrol",9800000)

C1.display()
C2.display()