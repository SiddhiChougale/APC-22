#college record management system
# 1

file=open("std.txt","w")

def add():
    file.write(input("Enter the name"))
    file.write(input("Enter roll no."))
    print("Record successfully")

def display():
    print(file.read())



while True:
    print("1. Add Student")
    print("2. Display Students")

    try:
        ch=input("enter the choice: ")

        if ch==1:
            add()

        elif ch==2:
            display()

        else:
            print("invalid choice")

    except ValueError:
            print("Please enter a number.")

file.close()