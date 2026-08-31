f = open("student.txt", "r")

lines = f.readlines()

for line in reversed(lines):
    print(line)

f.close()
