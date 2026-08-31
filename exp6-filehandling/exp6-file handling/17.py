f = open("file.txt", "r")

lines = f.readlines()
f.close()

students = []

for line in lines[1:]:
    data = line.strip().split(",")
    roll = data[0]
    name = data[1]
    marks = int(data[2])
    students.append([roll, name, marks])

# Display all records
print("All Records:")
for s in students:
    print(s)

# Highest marks
highest = max(students, key=lambda x: x[2])
print("Highest marks:", highest[1])

# Average marks
total = 0
for s in students:
    total = total + s[2]

average = total / len(students)
print("Average marks:", average)

# Students scoring more than 80
print("Students scoring more than 80:")
for s in students:
    if s[2] > 80:
        print(s[1])
