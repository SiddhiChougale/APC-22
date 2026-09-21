class Emplyoee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary

    def display(self):
        print("id: ",self.id) 
        print("name: ",self.name)
        print("Salary: ",self.salary)

class Manager(Emplyoee):
    def __init__(self, id, name, salary,department):
        super().__init__(id, name, salary)
        self.department=department

    def display(self):
        super().display()
        print("Deartment: ",self.department)
        print("Anual salary: ",self.salary*12)

m=Manager(101,"Priya",48000,"IT")
m.display()