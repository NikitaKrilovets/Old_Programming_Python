# Task 5 - Krilovets - IT-31

birth_day = 8
birth_month = 5

first_positive = birth_day > 0
first_even = birth_day % 2 == 0
first_both = first_positive and first_even

second_number = birth_day * birth_month

second_positive = second_number > 0
second_even = second_number % 2 == 0
second_both = second_positive and second_even

print(f"Birth day is positive: {first_positive}")
print(f"Birth day is even: {first_even}")
print(f"Both conditions are true: {first_both}")

print(f"Product of birth day and month: {second_number}")
print(f"Product is positive: {second_positive}")
print(f"Product is even: {second_even}")
print(f"Both conditions are true: {second_both}")