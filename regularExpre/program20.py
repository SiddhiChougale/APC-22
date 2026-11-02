import re
text = "Files: notes.txt photo.jpg program.py"
result = re.findall(r'\b[\w-]+\.([A-Za-z0-9]+)\b', text)
print(result)