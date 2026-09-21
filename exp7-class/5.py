class Book:
    def  __init__(self,id,title,author,price):
        self.id=id
        self.title=title
        self.author=author
        self.price=price

    def display(self):
            print("Id: ",self.id)
            print("Title: ",self.title)
            print("Author: ",self.author)
            print("Price: ",self.price)
            print("-----")

b1=Book(101,"abc","xyz",75)
b2=Book(102,"pqr","lmn",90)
b3=Book(103,"ijk","rst",89)

b1.display()
b2.display()
b3.display()