def display():
    f = open("emp.txt", "r")

    for line in f:
        print(line)

    f.close()


def highest_salary():
    f = open("emp.txt", "r")

    highest = 0
    name = ""

    for line in f:
        data = line.strip().split(",")
        salary = int(data[3])

        if salary > highest:
            highest = salary
            name = data[1]

    print("Highest-paid employee:", name)
    print("Salary:", highest)

    f.close()


def average_salary():
    f = open("emp.txt", "r")

    total = 0
    count = 0

    for line in f:
        data = line.strip().split(",")
        total = total + int(data[3])
        count = count + 1

    print("Average salary:", total / count)

    f.close()


def above_salary(amount):
    f = open("emp.txt", "r")

    for line in f:
        data = line.strip().split(",")
        if int(data[3]) > amount:
            print(data[1])

    f.close()


display()
highest_salary()
average_salary()

salary = int(input("Enter salary: "))
above_salary(salary)
