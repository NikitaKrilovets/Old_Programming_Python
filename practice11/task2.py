name = "Nikita"
surname = "Krilovets"
group = "IT-31"
y = 2009

print(f"{name} {surname}, {group}")


def print_age(year):
    age = 2026 - year
    print(f"Age: {age}")

result = print_age(y)


def get_age(year, current_year = 2026):
    if year > current_year or year < 0:
        return -1

    age = current_year - year
    return age
    print("after return")

print(f"print_age returned: {result}")



age = get_age(y)
print(f"Age from get_age: {age}")

months = age * 12
weeks = age * 52

print(f"Age in months: {months}")
print(f"Age in weeks: {weeks}")


age_2030 = get_age(y, 2030)
print(f"Age in 2030: {age_2030}")


invalid_age = get_age(3000)
print(f"Invalid year 3000 gives: {invalid_age}")