# Students in two courses
course1 = {"Amit", "Rahul", "Sneha", "Priya"}
course2 = {"Rahul", "Priya", "Karan", "Neha"}

# Students enrolled in both courses
both_courses = course1 & course2

# Students enrolled in only one course
only_one_course = course1 ^ course2

print("Students in both courses:", both_courses)
print("Students in only one course:", only_one_course)
