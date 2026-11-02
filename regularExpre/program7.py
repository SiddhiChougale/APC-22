import re
text = input("Enter a sentence: ")
result = re.findall(r'\b[A-Za-z]{5}\b', text)
print(result)