f = open("student.txt", "r")

text = f.read()
words = text.split()

longest = max(words, key=len)

print("Longest word:", longest)

f.close()
