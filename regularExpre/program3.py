import re
text = input("Enter a string: ")
result = re.findall(r'[aeiouAEIOU]', text)
print("Vowel count:", len(result))