import re
text = "My PIN is 416003 and another is 110001"
result = re.findall(r'(?<!\d)[1-9]\d{5}(?!\d)', text)
print(result)