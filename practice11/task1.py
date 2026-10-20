name = "Nikita"
surname = "Krilovets"
group = "IT-31"
year = 2009

def print_card():
    print(f"{name} {surname}", end=", ")
    print(group)

print_card()

def print_card_args(name, surname, group, year):
    print(f"Name: {name} {surname}\nGroup: {group}\nBirth year: {year}")

print("--- no parameters, call 1 ---")
print_card_args(name, surname, group, year)

print("--- no parameters, call 2 ---")
print_card_args(name, surname, group, year)

print("--- no parameters, call 3 ---")
print_card_args(name, surname, group, year)



def print_card_args(name, surname, group, year):
    print(f"{name} {surname}, {group}, {year}")

print("--- positional arguments ---")
print_card_args("Nikita", "Krilovets", "IT-31", 2009)


print("--- keyword arguments ---")
print_card_args(name="Nikita", surname="Krilovets", group="IT-31", year=2009)


print("--- default group ---")
print_card_args("Nikita", "Krilovets", "IT-31", 2009)