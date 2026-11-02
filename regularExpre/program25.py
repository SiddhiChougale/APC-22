import re
text = """
Name: Rahul, Roll: 101, Marks: 85
Name: Priya, Roll: 102, Marks: 92
"""
pattern = r'Name:\s*(\w+),\s*Roll:\s*(\d+),\s*Marks:\s*(\d+)'
result = re.findall(pattern, text)
for name, roll, marks in result:
    print("Name:", name)
    print("Roll Number:", roll)
    print("Marks:", marks)