# Пункт 1
from pathlib import Path
from datetime import datetime


def count_runs(path):
    if not path.exists():
        return 0

    with path.open("r", encoding="utf-8") as file:
        lines = file.readlines()

    return len([line for line in lines if line.strip()])


# Пункт 2
def add_run(path, number):
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with path.open("a", encoding="utf-8") as file:
        file.write(f"{number};{stamp};Nikita Krilovets\n")

#Пункт 3
def show_history(path, last=3):
    with path.open("r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]

    print("runs so far:", len(lines))
    print("last runs:")

    for line in lines[-last:]:
        number, stamp, name = line.split(";")
        print(number, stamp, name)

    first = lines[0].split(";")
    print("first run was at:", first[1])

#Пункт 4
def main():
    path = Path(__file__).resolve().parent / "data" / "runs.log"

    runs = count_runs(path)
    run_number = runs + 1

    add_run(path, run_number)

    print(f"Hello, Nikita Krilovets! This is run number {run_number}.")

    if run_number == 1:
        print("runs.log was just created.")

    show_history(path)
    
main()