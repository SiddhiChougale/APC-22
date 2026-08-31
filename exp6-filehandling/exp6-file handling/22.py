f1 = open("student.txt", "r")
text1 = f1.read()
f1.close()

f2 = open("att.txt", "r")
text2 = f2.read()
f2.close()

f3 = open("file.txt", "w")

f3.write(text1)
f3.write("\n")
f3.write(text2)

f3.close()

print("Files combined successfully.")
