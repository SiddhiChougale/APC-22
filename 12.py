sentence = input("Enter a sentence: ")

words = sentence.split()

if words:
    longest_word = max(words, key=len)
    print(f"The longest word is: ",longest_word )
else:
    print("No words found.")
