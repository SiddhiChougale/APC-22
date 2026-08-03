def count_string_elements(text):
    vowels = consonants = digits = spaces = special_chars = 0 
    
    vowel_set = set("aeiouAEIOU")
    
    for char in text:
        if char.isalpha():
            if char in vowel_set:
                vowels += 1
            else:
                consonants += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        else:
            special_chars += 1
            
    # Display the results
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    print(f"Digits: {digits}")
    print(f"Spaces: {spaces}")
    print(f"Special Characters: {special_chars}")

input_string = input("enter the string")
print(f"Analyzing: '{input_string}'")
count_string_elements(input_string)
