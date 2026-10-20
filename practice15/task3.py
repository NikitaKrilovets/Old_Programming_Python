# Nikita Krilovets, IT-31

def print_header():
    print("Nikita Krilovets, IT-31")
    print("#  Subject             Pairs  Grade")


def print_subjects(subjects):
    for i, subject in enumerate(subjects, 1):
        title, pairs, grade = subject
        print(f"{i:<3}{title:<20}{pairs:<7}{grade}")


def total_pairs(subjects):
    return sum(subject[1] for subject in subjects)


def most_pairs_subject(subjects):
    return max(subjects, key=lambda subject: subject[1])


def weakest_subject(subjects):
    return min(subjects, key=lambda subject: subject[2])


def get_titles(subjects):
    return [subject[0] for subject in subjects]


def get_grades(subjects):
    return [subject[2] for subject in subjects]


def average_grade(subjects):
    grades = get_grades(subjects)
    return sum(grades) / len(grades)


def print_grade_10_plus(subjects):
    result = [subject[0] for subject in subjects if subject[2] >= 10]
    print("Grade 10+:", result)


def print_histograms(subjects):
    for title, pairs, grade in subjects:
        print(f"{title}: {'#' * grade}")


def retake_lowest(subjects):
    weakest = weakest_subject(subjects)
    old_grade = weakest[2]
    new_grade = min(old_grade + 2, 12)

    new_subjects = []

    for subject in subjects:
        if subject == weakest:
            new_subjects.append((subject[0], subject[1], new_grade))
        else:
            new_subjects.append(subject)

    print(f"Retake: {weakest[0]} {old_grade} -> {new_grade}")

    return new_subjects


def main():
    subjects = [
        ("Programming", 3, 11),
        ("Math", 2, 9),
        ("English", 2, 10),
        ("Physics", 1, 7),
        ("Ukrainian", 2, 12),
        ("Databases", 2, 10)
    ]

    print_header()
    print_subjects(subjects)

    print("Pairs per week:", total_pairs(subjects))

    most = most_pairs_subject(subjects)
    print(f"Most pairs: {most[0]} ({most[1]})")

    weakest = weakest_subject(subjects)
    print(f"Weakest subject: {weakest[0]} ({weakest[2]})")

    titles = get_titles(subjects)
    grades = get_grades(subjects)

    print("Titles:", titles)
    print("Grades:", grades)
    print(f"Average: {average_grade(subjects):.2f}")

    print_grade_10_plus(subjects)

    print_histograms(subjects)

    subjects = retake_lowest(subjects)

    print("Subjects:", subjects)


main()