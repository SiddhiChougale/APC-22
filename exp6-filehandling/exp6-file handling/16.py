f = open("student.txt", "r")
text = f.read()
f.close()

f = open("upper.txt", "w")
f.write(text.upper())
f.close()

print("Uppercase file created.")
