sentence = input("Enter a sentence: ")

words = sentence.split()

if words:
    smallest_word = min(words, key=len)
    print(f"The longest word is: ",smallest_word )
else:
    print("No words found.")
