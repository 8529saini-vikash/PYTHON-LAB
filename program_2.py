import re

text = input("Enter text: ")

words = re.findall(r'\b\w+\b', text.lower())

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

palindromes = []

for word in frequency:
    if len(word) > 1 and word == word[::-1]:
        palindromes.append(word)

print("\nTotal words:", len(words))

print("\nWord Frequency:")
for word, count in frequency.items():
    print(word, ":", count)

print("\nPalindromes:")
if palindromes:
    for word in palindromes:
        print(word)
else:
    print("None")