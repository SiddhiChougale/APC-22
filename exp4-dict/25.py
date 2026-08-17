students = {
    "Amit": 75,
    "Rahul": 85,
    "Sneha": 90
}

while True:
    print("\n1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. Search Student")
    print("5. Display All Students")
    print("6. Find Highest Marks")
    print("7. Calculate Average")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added.")

    elif choice == 2:
        name = input("Enter student name: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated.")
        else:
            print("Student not found.")

    elif choice == 3:
        name = input("Enter student name: ")
        if name in students:
            del students[name]
            print("Student deleted.")
        else:
            print("Student not found.")

    elif choice == 4:
        name = input("Enter student name: ")
        if name in students:
            print("Marks:", students[name])
        else:
            print("Student not found.")

    elif choice == 5:
        for name, marks in students.items():
            print(name, ":", marks)

    elif choice == 6:
        if students:
            name = max(students, key=students.get)
            print("Highest marks:", name, students[name])
        else:
            print("No students available.")

    elif choice == 7:
        if students:
            average = sum(students.values()) / len(students)
            print("Average marks:", average)
        else:
            print("No students available.")

    elif choice == 8:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
