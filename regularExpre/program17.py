import re
text = input("Enter a sentence: ")
result = re.findall(
    r'\b(\w+)\s+\1\b',
    text,
    re.IGNORECASE
)
print(result)