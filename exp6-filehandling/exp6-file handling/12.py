f = open("student.txt", "r")

text = f.read()
words = text.split()

count = {}

for word in words:
    if word in count:
        count[word] = count[word] + 1
    else:
        count[word] = 1

print(count)

f.close()
