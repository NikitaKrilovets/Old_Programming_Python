schedule = {
    "Mon": ["Programming", "Ukrainian language", "OS administration"],
    "Tue": ["Programming", "IT-law", "Data Base"],
    "Wed": ["English language", "Data Base", "Web resource development"],
    "Thu": ["Programming", "Web resource development", "OS administration"],
    "Fri": ["English language", "Web resource development", "IT-law"]
}


for day, subjects in schedule.items():
    print(f"{day}: {len(subjects)} pairs - {', '.join(subjects)}")


total_pairs = sum(len(subjects) for subjects in schedule.values())
print("Total pairs:", total_pairs)


max_day = max(schedule, key=lambda day: len(schedule[day]))
print("Day with most pairs:", max_day)


all_subjects = set()

for subjects in schedule.values():
    all_subjects.update(subjects)

print("All different subjects:", all_subjects)
print("Number of subjects:", len(all_subjects))


monday = set(schedule["Mon"])
wednesday = set(schedule["Wed"])

print("In Monday and Wednesday:", monday & wednesday)
print("In Monday but not Wednesday:", monday - wednesday)


def count_subjects(schedule):
    result = {}

    for subjects in schedule.values():
        for subject in subjects:
            result[subject] = result.get(subject, 0) + 1

    return result


subject_counts = count_subjects(schedule)

print("Subject counts:", subject_counts)


rating = sorted(
    subject_counts.items(),
    key=lambda item: item[1],
    reverse=True
)

for number, (subject, count) in enumerate(rating, 1):
    print(f"{number}. {subject} - {count}")