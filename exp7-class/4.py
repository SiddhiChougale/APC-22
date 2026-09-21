class Circle:
    def __init__(self,r):
        self.r=r

    def display(self):
        area=3.14*self.r*self.r
        cir=2*3.14*self.r  
        print("Area: ",area)
        print("Circumference: ",cir)
        print("-----")

c1=Circle(5)
c2=Circle(24)

c1.display()
c2.display()