text = input("Enter a string: ")

unique_text = "".join(dict.fromkeys(text))

print(f"Result: {unique_text}")
