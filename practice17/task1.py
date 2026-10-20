me = {
    "name": "Nikita",
    "surname": "Krilovets",
    "group": "IT-31",
    "city": "Lutsk",
    "birth_year": 2009,
    "hobbies": ["football", "pianino", "swim"]
}

for key, value in me.items():
    print(f"{key}: {value}")

print("Keys:", list(me.keys()))
print("Number of pairs:", len(me))

print("Group:", me["group"])
print("Email:", me.get("email", "unknown"))

# me["email"] викликало б помилку KeyError, бо такого ключа ще немає.

me["email"] = "nikita@example.com"

me["city"] = "Kyiv"

birth_year = me.pop("birth_year")
print("Removed birth year:", birth_year)

print("Final dictionary:", me)

print("Phone:", "phone" in me)