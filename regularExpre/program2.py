import re
text = input("Enter a sentence: ")
result = re.findall(r'\b[Aa]\w*', text)
print(result)