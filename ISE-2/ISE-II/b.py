
def process_string():
    text = "Hello Python ProgrAm"

    vowels = "aeiouAEIOU"
    vowel_count = 0
    

    for ch in text:
        if ch in vowels:
            vowel_count += 1

    print("Vowel:",vowel_count)

try:
    process_string()

except Exception as e:
    print("Error:", e)





















# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0

#     for char in text:
#         if char in vowels:
#             count += 1

#     return count
