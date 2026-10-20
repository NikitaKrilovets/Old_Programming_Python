about = "I study Python and frontend development at college every day."

words = about.split()

print("Number of words:", len(words))

longest_word = max(words, key=len)
print("Longest word:", longest_word)

print("Words backwards:", " ".join(words[::-1]))

print("Number of letter 'a':", about.lower().count("a"))

print("Capitalized:", about.title())

print("With underscores:", about.replace(" ", "_"))


def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]


print("Is my name a palindrome:", is_palindrome("Nikita"))
print("Is 'Never odd or even' a palindrome:",
      is_palindrome("Never odd or even"))


def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


day = 8
name = "Nikita"

encrypted = caesar_encrypt(name, day)
decrypted = caesar_decrypt(encrypted, day)

print("Original name:", name)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)