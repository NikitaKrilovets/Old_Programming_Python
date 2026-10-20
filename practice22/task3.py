import sys


def add_expense(category, amount):
    with open("expenses.txt", "a", encoding="utf-8") as file:
        file.write(f"{category};{amount}\n")


def list_expenses():
    with open("expenses.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            print(line)


def report_expenses():
    total = 0

    with open("expenses.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            category, amount = line.split(";")
            total += float(amount)

    print("Загальна сума:", total)


if len(sys.argv) < 2:
    print("Usage: python task3.py add/list/report")
    sys.exit()
    
command = sys.argv[1]

if command == "add":
    if len(sys.argv) < 4:
        print("Usage: python task3.py add \"категорія\" сума")
        sys.exit()

    category = sys.argv[2]
    amount = sys.argv[3]

    add_expense(category, amount)
    print("Витрату додано")

elif command == "list":
    list_expenses()

elif command == "report":
    report_expenses()

else:
    print("Невідома команда")