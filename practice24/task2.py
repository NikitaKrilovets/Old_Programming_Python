
import sys
import shutil
from pathlib import Path

print("Nikita Krilovets, IT-31")


def main():
    args = sys.argv[1:]
    force = False

    if "--force" in args:
        force = True
        args.remove("--force")

    if len(args) != 2:
        print(
            "Використання: python task2.py [--force] <джерело> <призначення>",
            file=sys.stderr
        )
        return 2

    source = Path(args[0])
    destination = Path(args[1])

    try:
        if not source.exists():
            raise FileNotFoundError(f"Джерело не знайдено: {source}")

        if source.is_dir():
            raise IsADirectoryError(f"Джерело є папкою: {source}")

        if not destination.parent.exists():
            raise FileNotFoundError(
                f"Папка призначення не існує: {destination.parent}"
            )

        if destination.is_dir():
            raise IsADirectoryError(
                f"Призначення є папкою: {destination}"
            )

        if source.resolve() == destination.resolve():
            raise shutil.SameFileError("Джерело та призначення — той самий файл")

        if destination.exists() and not force:
            raise FileExistsError(
                f"Файл уже існує: {destination}. Використай --force"
            )

        shutil.copy2(source, destination)
        print(f"Файл скопійовано: {source} -> {destination}")
        return 0

    except shutil.SameFileError as error:
        print(f"Помилка: {error}", file=sys.stderr)
        return 1
    except (OSError, shutil.Error) as error:
        print(f"Помилка копіювання: {type(error).__name__}: {error}",
              file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
