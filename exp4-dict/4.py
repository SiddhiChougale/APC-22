marks = {
    "Amit": 75,
    "Rahul": 80,
    "Sneha": 90
}

name = input("Enter student name: ")
new_marks = int(input("Enter new marks: "))

marks[name] = new_marks

print(marks)
