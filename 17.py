str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

clean_str1 = str1.replace(" ", "").lower()
clean_str2 = str2.replace(" ", "").lower()

if sorted(clean_str1) == sorted(clean_str2):
    print("The strings are anagrams!")
else:
    print("The strings are not anagrams.")
