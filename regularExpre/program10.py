import re
text = input("Enter a sentence: ")
result = re.findall(r'\b\w+\b', text)
print("Word count:", len(result))