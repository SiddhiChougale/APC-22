employees = {
    101: "Amit",
    102: "Rahul",
    103: "Sneha"
}

emp_id = int(input("Enter employee ID: "))

if emp_id in employees:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")
