import re
password = input("Enter password: ")
pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9\s]).{8,}'
if re.fullmatch(pattern, password):
    print("Valid password")
else:
    print("Invalid password")