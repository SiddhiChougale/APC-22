class Shape:
    def display_name(self):
        print("This is a Shape")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


C = Circle(5)
R = Rectangle(10, 5)
T = Triangle(8, 6)

C.display_name()
print("Circle Area:", C.area())

R.display_name()
print("Rectangle Area:", R.area())

T.display_name()
print("Triangle Area:", T.area())
