# Nikita Krilovets, IT-31

letters = list("krilovets")

print("Letters:", letters)
print("Length:", len(letters))

print("First letter:", letters[0])
print("Middle letter:", letters[len(letters) // 2])
print("Last letter:", letters[-1])
print("Last letter:", letters[len(letters) - 1])

print("First three:", letters[:3])
print("Except first three:", letters[3:])
print("Every second letter:", letters[::2])
print("Reverse:", letters[::-1])
print("Last two:", letters[-2:])

# c = 9, therefore position 9 does not exist in an 9-letter surname.
# To avoid an empty result, use the last valid position.
print("Part of length 5 from position 9:", letters[8:13])

unique = []

for letter in letters:
    if letter not in unique:
        unique.append(letter)

print("Unique letters:", unique)

has_repeated = False

for letter in unique:
    count = letters.count(letter)

    if count > 1:
        print("Letter", letter, "repeats", count, "times")
        has_repeated = True

if not has_repeated:
    print("No repeated letters")

print("Alphabetical order:", sorted(letters))