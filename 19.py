main_string = input("Enter the main string: ")
substring = input("Enter the substring to search for: ")

if substring in main_string:
    print(f"Yes, '{substring}' exists in the main string.")
else:
    print(f"No, '{substring}' does not exist in the main string.")
