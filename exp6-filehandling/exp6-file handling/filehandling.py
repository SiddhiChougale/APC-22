#1
file=open("student.txt","w")

file.write("Name:Siddhi Chougale \n")
file.write("Roll No.: 22 \n")
file.write("Branch:CSE \n")
file.write("Semester:V \n")
file.close()

print("Student file created")

#2
f=open("student.txt","r")
print(f.read())
f.close()

#3
f = open("student.txt", "a")
f.write("CGPA:8.4 \n")
f.close()
print("Append successful")

#4
f = open("student.txt", "r")

for line in f:
    print(line)

f.close()

#5
f=open("student.txt", "r")
count = 0
for line in f:
    count = count + 1
print("Total lines:", count)
f.close()

#6
f=open("student.txt","r")

text=f.read()
words=text.split()
print("Total words: ",len(words))
f.close()

#7
f = open("student.txt", "r")
text = f.read()
print("Total characters:", len(text))
f.close()

38
f = open("student.txt", "r")

lines = f.readlines()

for line in reversed(lines):
    print(line)

f.close()

#9
f = open("student.txt", "r")

text = f.read().lower()

v = 0
c= 0

for ch in text:
    if ch in "aeiou":
        v+=1
    elif ch.isalpha():
        c+=1

print("Vowels:", v)
print("Consonants:", c)

f.close()

#10 
f = open("student.txt", "r")
text = f.read()

alphabets = 0
digits = 0
spaces = 0
special = 0

for ch in text:
    if ch.isalpha():
        alphabets = alphabets + 1
    elif ch.isdigit():
        digits = digits + 1
    elif ch == " ":
        spaces = spaces + 1
    else:
        special = special + 1

print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

f.close()

#11 
f = open("student.txt", "r")

text = f.read()
words = text.split()

longest = max(words, key=len)

print("Longest word:", longest)

f.close()

#12
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

#13
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

#14
f = open("student.txt", "r")
text = f.read()
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")
text = text.replace(old_word, new_word)
f.close()
f = open("student.txt", "w")
f.write(text)
f.close()
print("Word replaced successfully.")

#15