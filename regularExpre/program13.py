import re
text = "Dates are 15-08-2026 and 26-01-2027"
result = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', text)
print(result)