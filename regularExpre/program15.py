import re
text = "I love #Python and #Programming"
result = re.findall(r'(?<!\w)#[A-Za-z0-9_]+', text)
print(result)