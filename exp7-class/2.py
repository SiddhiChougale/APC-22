class Emplyoee:
    def __init__(self,emp_id,name,basic_salary):
        self.emp_id=emp_id
        self.name=name
        self.basic_salary=basic_salary

    def HRA(self):
        return self.basic_salary *0.20

    def DA(self):
        return self.basic_salary*0.10

    def gross_salary(self):
        return self.basic_salary+self.HRA()+self.DA()

    def display(self):
        print("Emplyoee id: ",self.emp_id)
        print("Name: ",self.name)
        print("Salary: ",self.basic_salary)
        print("HRA: ",self.HRA())
        print("DA: ",self.DA())
        print("Gross Salary: ",self.gross_salary())
        print("------")



E1=Emplyoee(2364,"Priya",10000)
E2=Emplyoee(2635,"Megha",9500)

E1.display()
E2.display()