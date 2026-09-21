class Rectangle:
    def __init__(self,len,br):
        self.len=len
        self.br=br

    def area(self):
        return self.len*self.br

    def perimeter(self):
        return self.len+self.br

    def display(self):
        print("Area: ",self.area())
        print("Perimeter: ",self.perimeter())
        print("----*----")

r1=Rectangle(25,20)
r2=Rectangle(72,48)

r1.display()
r2.display()