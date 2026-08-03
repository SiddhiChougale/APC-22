def palindrome(text):
    text = text.lower()
    return text == text[::-1]

print(palindrome("Radar"))  
print(palindrome("Python")) 
print(palindrome("navjvan"))