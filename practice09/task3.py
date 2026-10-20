name = "Nikita"
surname = "Krilovets"

text = name + surname

vowels = 0
consonants = 0

for letter in text.lower():
    if letter in "aeiouy":
        vowels += 1
    else:
        consonants += 1

print(f"{name} {surname}")
print(f"Vowels: {vowels}, consonants: {consonants}")
print(f"Total letters: {len(text)}")