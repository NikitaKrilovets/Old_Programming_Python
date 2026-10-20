name = "Nikita"
surname = "Krilovets"
c = 9


def get_initials(name: str, surname: str) -> str:
    return name[0] + "." + surname[0] + "."


def count_letters(text: str, letter: str = "a") -> int:
    """Return how many times letter occurs in text."""

    count = 0

    for char in text.lower():
        if char == letter.lower():
            count += 1

    return count


def count_vowels(text: str) -> int:
    vowels = 0

    for char in text.lower():
        if char in "aeiouy":
            vowels += 1

    return vowels


def reverse_text(text: str) -> str:
    result = ""

    for char in text:
        result = char + result

    return result


print(f"{name} {surname}")
print(f"Initials: {get_initials(name, surname)}")
print(f"Letters in surname: {c}")

vowels = count_vowels(surname)
consonants = c - vowels

print(f"Vowels: {vowels}, consonants: {consonants}")

for vowel in "aeiou":
    amount = count_letters(surname, letter=vowel)
    print(f"{vowel}: {amount}")

print(f"Default letter 'a': {count_letters(surname)}")
print(f"Reversed surname: {reverse_text(surname)}")

print(f"Docstring: {count_letters.__doc__}")
print(f"Annotations: {count_letters.__annotations__}")