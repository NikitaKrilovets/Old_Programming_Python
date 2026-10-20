
import sys
from pathlib import Path
from datetime import datetime
from decimal import Decimal, InvalidOperation

print("Nikita Krilovets, IT-31")

DATA_FILE = Path("data/expenses.csv")
HEADER = "date;category;amount;note"


def validate_expense(date, category, amount, note):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("неправильна дата, потрібен формат YYYY-MM-DD")

    if not category.strip():
        raise ValueError("категорія не може бути порожньою")

    if not note.strip():
        raise ValueError("примітка не може бути порожньою")

    if any(";" in field for field in (date, category, amount, note)):
        raise ValueError("поля не повинні містити символ ';'")

    try:
        value = Decimal(amount)
    except InvalidOperation:
        raise ValueError("сума має бути числом")

    if not value.is_finite() or value <= 0:
        raise ValueError("сума повинна бути більшою за нуль")

    return value


def read_expenses():
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            lines = file.readlines()

        if not lines:
            raise ValueError("файл не містить заголовка")

        if lines[0].strip() != HEADER:
            raise ValueError("неправильний заголовок файлу")

        expenses = []
        skipped = []

        for line_number, line in enumerate(lines[1:], start=2):
            line = line.rstrip("\r\n")

            if not line.strip():
                skipped.append((line_number, "порожній рядок"))
                continue

            fields = line.split(";")

            if len(fields) != 4:
                skipped.append((line_number, "потрібно 4 поля"))
                continue

            date, category, amount, note = fields

            try:
                value = validate_expense(date, category, amount, note)
            except ValueError as error:
                skipped.append((line_number, str(error)))
                continue

            expenses.append({
                "date": date,
                "category": category,
                "amount": value,
                "note": note
            })

        return expenses, skipped, None

    except (OSError, UnicodeError, ValueError) as error:
        return None, [], error


def show_skipped(skipped):
    for line_number, reason in skipped:
        print(
            f"Пропущено рядок {line_number}: {reason}",
            file=sys.stderr
        )

    if skipped:
        print(
            f"Усього пропущено рядків: {len(skipped)}",
            file=sys.stderr
        )


def list_expenses():
    expenses, skipped, error = read_expenses()

    if error:
        print(
            f"Помилка файлу: {type(error).__name__}: {error}",
            file=sys.stderr
        )
        return 1

    if not expenses:
        print("Немає коректних витрат.")

    for expense in expenses:
        print(
            f'{expense["date"]} | {expense["category"]} | '
            f'{expense["amount"]:.2f} | {expense["note"]}'
        )

    show_skipped(skipped)
    return 0


def report_expenses():
    expenses, skipped, error = read_expenses()

    if error:
        print(
            f"Помилка файлу: {type(error).__name__}: {error}",
            file=sys.stderr
        )
        return 1

    if not expenses:
        print("Немає коректних витрат для звіту.")
        show_skipped(skipped)
        return 1

    total = sum(
        (expense["amount"] for expense in expenses),
        Decimal("0")
    )

    print(f"Кількість витрат: {len(expenses)}")
    print(f"Загальна сума: {total:.2f}")

    categories = {}

    for expense in expenses:
        category = expense["category"]
        categories[category] = (
            categories.get(category, Decimal("0")) + expense["amount"]
        )

    print("Суми за категоріями:")

    for category, amount in categories.items():
        print(f"{category}: {amount:.2f}")

    show_skipped(skipped)
    return 0


def add_expense(args):
    if len(args) != 4:
        print(
            "Використання: python task3.py add <дата> <категорія> "
            "<сума> <примітка>",
            file=sys.stderr
        )
        return 2

    date, category, amount, note = args

    try:
        value = validate_expense(date, category, amount, note)
    except ValueError as error:
        print(f"Некоректні дані: {error}", file=sys.stderr)
        return 1

    expenses, _, error = read_expenses()

    if error:
        print(
            f"Помилка файлу: {type(error).__name__}: {error}",
            file=sys.stderr
        )
        return 1

    try:
        with DATA_FILE.open("a", encoding="utf-8") as file:
            file.write(
                f"{date};{category};{value:.2f};{note}\n"
            )
    except (OSError, UnicodeError) as error:
        print(
            f"Не вдалося записати файл: {type(error).__name__}: {error}",
            file=sys.stderr
        )
        return 1

    print("Витрату додано.")
    return 0


def main():
    if len(sys.argv) < 2:
        print(
            "Використання: python task3.py add/list/report",
            file=sys.stderr
        )
        return 2

    command = sys.argv[1]

    if command == "add":
        return add_expense(sys.argv[2:])
    elif command == "list":
        if len(sys.argv) != 2:
            print("Використання: python task3.py list", file=sys.stderr)
            return 2
        return list_expenses()
    elif command == "report":
        if len(sys.argv) != 2:
            print("Використання: python task3.py report", file=sys.stderr)
            return 2
        return report_expenses()
    else:
        print(f"Невідома команда: {command}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
