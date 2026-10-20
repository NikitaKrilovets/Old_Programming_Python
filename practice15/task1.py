# Nikita Krilovets, IT-31

grades = [11, 9, 10, 8, 12, 7, 10, 9, 11]

print("Grades:", grades)
print("Number of grades:", len(grades))
print("Sum:", sum(grades))
print("Best grade:", max(grades))
print("Worst grade:", min(grades))
print("Average: {:.2f}".format(sum(grades) / len(grades)))

print("Sorted grades:", sorted(grades, reverse = True))
print("Original grades:", grades)

print("Three best:", sorted(grades, reverse = True)[:3])
print("Three worst:", sorted(grades)[:3])

print("Position of worst grade:", grades.index(min(grades)) + 1)

above_average = [grade for grade in grades if grade > sum(grades) / len(grades)]
print("Above average:", above_average)
print("Number above average:", len(above_average))

print("Has 12:", 12 in grades)
print("Has 1:", 1 in grades)

grades.append(9 % 12 + 1)
print("After adding to the end:", grades)

grades.insert(0, 12)
print("After inserting 12 at the beginning:", grades)

grades.remove(min(grades))
print("After removing the worst grade:", grades)

removed = grades.pop()
print("Removed last grade:", removed)
print("After removing the last grade:", grades)

print("Number of 12:", grades.count(12))

result = grades.sort()
print("Sort returned:", result)
print("Grades after sort:", grades)