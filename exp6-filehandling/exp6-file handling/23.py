f1 = open("student.txt", "r")
f2 = open("file.txt", "r")

line1 = f1.readline()
line2 = f2.readline()

line_no = 1

while line1 != "" and line2 != "":
    if line1 != line2:
        print("Files are different.")
        print("First difference is at line:", line_no)
        break

    line1 = f1.readline()
    line2 = f2.readline()
    line_no = line_no + 1

else:
    if line1 == line2:
        print("Files are identical.")
    else:
        print("Files are different.")
        print("First difference is at line:", line_no)

f1.close()
f2.close()
