class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary


class Manager(Employee):
    def calculate_salary(self):
        allowance = self.basic_salary * 0.30
        return self.basic_salary + allowance


class Developer(Employee):
    def calculate_salary(self):
        allowance = self.basic_salary * 0.20
        return self.basic_salary + allowance


class Tester(Employee):
    def calculate_salary(self):
        allowance = self.basic_salary * 0.15
        return self.basic_salary + allowance


M = Manager(101, "Rahul", 50000)
D = Developer(102, "Amit", 45000)
T = Tester(103, "Priya", 40000)

print("Manager:", M.name)
print("Salary:", M.calculate_salary())
print("----")

print("Developer:", D.name)
print("Salary:", D.calculate_salary())
print("----")

print("Tester:", T.name)
print("Salary:", T.calculate_salary())
