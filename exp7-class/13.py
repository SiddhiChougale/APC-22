class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5

    def grade(self):
        p = self.percentage()

        if p >= 80:
            return "A"
        elif p >= 60:
            return "B"
        elif p >= 40:
            return "C"
        else:
            return "Fail"

    def __del__(self):
        print("Student result object destroyed")


s = StudentResult("Rahul", [80, 75, 90, 85, 70])

print("Name:", s.name)
print("Total:", s.total())
print("Percentage:", s.percentage(), "%")
print("Grade:", s.grade())
