text = input("Enter a string: ")

upper_count = 0
lower_count = 0

for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")
