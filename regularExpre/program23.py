import re

text = """
# This is a comment
x = 10  # Another comment
print("Hello # Python")
"""
result = re.findall(r'#.*', text)
print(result)