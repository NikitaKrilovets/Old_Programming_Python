full_name = "  kRILOVETS   nIKITA oLEKSIYOVYCH  "

full_name = " ".join(full_name.split()).title()

print("Full name:", full_name)
print("Length:", len(full_name))

surname, name, patronymic = full_name.split()

print("First letter of surname:", surname[0])
print("Last letter of surname:", surname[-1])
print("Surname backwards:", surname[::-1])

print("Name format:", f"{surname} {name[0]}. {patronymic[0]}.")
print("Initials:", f"{surname[0]}{name[0]}{patronymic[0]}")

vowels = "aeiouy"
vowels_count = sum(1 for char in full_name.lower() if char in vowels)

print("Number of vowels:", vowels_count)

group = "IT-31"

dash_position = group.find("-")

print("Before dash:", group[:dash_position])
print("After dash:", group[dash_position + 1:])
print("Is number:", group[dash_position + 1:].isdigit())

login = f"{name[0].lower()}.{surname.lower()}"
email = f"{login}@student.edu.ua"

print("Login:", login)
print("Email:", email)