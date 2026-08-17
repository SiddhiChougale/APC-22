marks = {
    "Amit": 75,
    "Rahul": 90,
    "Sneha": 85,
    "Priya": 95
}

lowest_student = min(marks, key=marks.get)

print("Lowest marks:", lowest_student)
print("Marks:", marks[lowest_student])
