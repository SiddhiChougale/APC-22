marks = {
    "Amit": 75,
    "Rahul": 90,
    "Sneha": 85,
    "Priya": 95
}

highest_student = max(marks, key=marks.get)

print("Highest marks:", highest_student)
print("Marks:", marks[highest_student])
