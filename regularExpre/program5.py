import re
text = "Hello World\tPython\nProgramming"
result = re.findall(r'[ \t\n]', text)
print(result)
print("Count:", len(result))