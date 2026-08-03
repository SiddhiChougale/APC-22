sentence = input("Enter a sentence: ")
target_word = input("Enter the word to count: ")

words = sentence.split()

word_count = words.count(target_word)

print(f"The word '{target_word}' appears {word_count} times.")
