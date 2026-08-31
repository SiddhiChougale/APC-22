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
