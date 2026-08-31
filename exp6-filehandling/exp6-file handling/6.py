f=open("student.txt", "r")
count = 0
for line in f:
    count = count + 1
print("Total lines:", count)
f.close()
