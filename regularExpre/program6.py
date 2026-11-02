import re

text = "Python    is   very    easy"
result = re.sub(r' +', ' ', text)
print(result)