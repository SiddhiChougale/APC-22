text = input("Enter a string: ")

print("\nCharacter -> ASCII Value")
# print("------------------------")

for char in text:
    ascii_value = ord(char)
    print(f"'{char}'       -> {ascii_value}")
