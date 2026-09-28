class Academics:
    def __init__(self, mark):
        self.mark = mark


class Sports:
    def __init__(self, point):
        self.point = point


class Student(Academics, Sports):
    def __init__(self, mark, point):
        Academics.__init__(self, mark)
        Sports.__init__(self, point)

    def display(self):
        print("Marks:", self.mark)
        print("Sport points:", self.point)
        print("Total Marks:", self.mark + self.point)
        print("----")


S1 = Student(85, 9)
S2 = Student(76, 8)

S1.display()
S2.display()
