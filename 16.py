text = input("Enter a string: ")

frequency_dict = {}

for char in text:
    if char in frequency_dict:
        frequency_dict[char] += 1
    else:
        frequency_dict[char] = 1

print("\nCharacter Frequencies:")
for char, count in frequency_dict.items():
    print(f"'{char}': {count}")
