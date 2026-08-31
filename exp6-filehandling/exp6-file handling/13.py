f = open("student.txt", "r")
word = input("Enter word to search: ")
count = 0
line_no = 0
for line in f:
    line_no = line_no + 1
    words = line.split()

    for w in words:
        if w == word:
            count = count + 1
            print("Found in line:", line_no)
print("Total occurrences:", count)

f.close()
