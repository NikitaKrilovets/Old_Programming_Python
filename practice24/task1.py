
import sys
from pathlib import Path

print("Nikita Krilovets, IT-31")


def read_file(path):
    try:
        with path.open("r", encoding="utf-8") as file:
            lines = file.readlines()

        if not lines:
            raise ValueError("Файл порожній")

        print(f"{path}: рядків — {len(lines)}")
        print(f"Перший рядок: {lines[0].rstrip()}")

        return True

    except (OSError, UnicodeError, ValueError) as error:
        print(
            f"Помилка для {path}: {type(error).__name__}: {error}",
            file=sys.stderr
        )
        return False


def main():
    paths = sys.argv[1:]

    if not paths:
        print("Використання: python task1.py <шлях> [<шлях> ...]",
              file=sys.stderr)
        return 2

    success = True

    for item in paths:
        if not read_file(Path(item)):
            success = False

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
