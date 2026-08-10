students = ["Rahul", "Priya", "Amit", "Sneha", "Riya"]

# Total students
print("Total students:", len(students))

# Search a student's attendance
name = input("Enter student name to search: ")

if name in students:
    print(name, "is present.")
else:
    print(name, "is absent.")

# Add a new student
new_student = input("Enter new student name: ")
students.append(new_student)
print("Student added.")

# Remove an absent student
absent_student = input("Enter absent student name to remove: ")

if absent_student in students:
    students.remove(absent_student)
    print("Student removed.")
else:
    print("Student not found.")

# Display final list
print("Final student list:", students)