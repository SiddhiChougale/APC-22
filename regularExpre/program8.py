import re
text = input("Enter a sentence: ")
result = re.findall(r'\b\w+s\b', text, re.IGNORECASE)
print(result)