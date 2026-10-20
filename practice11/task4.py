def read_grade(prompt):
    """Reads a grade from 0 to 100."""
    while True:
        grade = input(prompt)

        if not grade.isdigit():
            print("Error: digits only")
            continue

        grade = int(grade)

        if grade < 0 or grade > 100:
            print("Error: the value must be between 0 and 100")
            continue

        return grade


def to_letter(grade):
    """Converts a numeric grade to a letter grade."""
    if grade >= 90:
        return "A"
    if grade >= 82:
        return "B"
    if grade >= 74:
        return "C"
    if grade >= 64:
        return "D"
    if grade >= 60:
        return "E"
    return "F"


def average(grades):
    """Returns the arithmetic mean of grades."""
    return sum(grades) / len(grades)


def count_above(grades, limit):
    """Counts grades greater than the given limit."""
    count = 0

    for grade in grades:
        if grade > limit:
            count += 1

    return count


def print_report(name, group, grades):
    """Prints the student grade report."""
    avg = average(grades)

    print("--- Report ---")
    print(f"Student: {name}, group {group}")
    print("Grades:", *grades)
    print(f"Average: {avg:.2f} -> {to_letter(avg)}")
    print(f"Best: {max(grades)}, worst: {min(grades)}")
    print(f"Above average: {count_above(grades, avg)}")


def main():
    """Runs the main program."""
    name = "Nikita"
    group = "IT-31"
    n = 6

    grades = []

    print(f"{name} {group}")

    for i in range(1, n + 1):
        grade = read_grade(f"Grade {i} (0-100): ")
        grades.append(grade)

    print_report(name, group, grades)

main()