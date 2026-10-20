grades_string = "90, 85, 95, 88, 92"

grades = [int(grade) for grade in grades_string.split(", ")]

print("Grades:", grades)
print("Average:", f"{sum(grades) / len(grades):.2f}")
print("Highest grade:", max(grades))
print("Lowest grade:", min(grades))

print("Grades:", " | ".join(str(grade) for grade in grades))

subjects_string = "Programming, Mathematics, English, Databases, Frontend"

subjects = subjects_string.split(", ")

print(f"{'No.':<5}{'Subject':<15}{'Grade':>5}")
print("-" * 25)

for number, (subject, grade) in enumerate(zip(subjects, grades), 1):
    print(f"{number:<5}{subject:<15}{grade:>5}")

longest_subject = max(subjects, key=len)

print("Longest subject:", longest_subject)
print("Number of characters:", len(longest_subject))