
def clean_text(text):
    return "".join(char.lower() for char in text if char.isalnum())


def count_characters(text):
    counts = {}
    for char in clean_text(text):
        counts[char] = counts.get(char, 0) + 1
    return counts


first = input("Enter the first word or phrase: ")
second = input("Enter the second word or phrase: ")

clean_first = clean_text(first)
clean_second = clean_text(second)

sorted_key_first = tuple(sorted(clean_first))
sorted_key_second = tuple(sorted(clean_second))

print("\nCleaned first text:", clean_first)
print("Cleaned second text:", clean_second)
print("Character counts:", count_characters(first))
print("Pattern key:", sorted_key_first)

if sorted_key_first == sorted_key_second:
    print("Result: The texts are anagrams.")
else:
    print("Result: The texts are not anagrams.")