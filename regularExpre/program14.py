import re
text = "Visit https://google.com and http://example.com"
result = re.findall(r'https?://[^\s]+', text)
print(result)