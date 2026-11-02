import re
text = "My roll number is 123 and marks are 90"
result = re.findall(r'\d', text)
print(result)