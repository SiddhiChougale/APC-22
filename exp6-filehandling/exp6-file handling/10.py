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
#printing
print("Alphabets:", alphabets)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

f.close()
