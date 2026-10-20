mark = int(input("Enter your mark: "))

if mark < 0 or mark > 101:
    print("Error")
    exit()

if mark >= 90 and mark <= 100:
    mark_letter = "A"

elif mark >= 82 and mark <= 89:
    mark_letter = "B"

elif mark >= 74 and mark <= 81:
    mark_letter = "C"

elif mark >= 64 and mark <= 73:
    mark_letter = "D"

elif mark >= 60 and mark <= 63:
    mark_letter = "E"

else:
    mark_letter = "F"

if mark >= 60:
    status = "passed"
else:
    status = "failed"

missed_classes = int(input("Enter your missed classes: "))

print(f"Your mark is {mark}, your letter mark is {mark_letter} and your status is {status}")