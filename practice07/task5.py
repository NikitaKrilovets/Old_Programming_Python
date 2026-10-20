d = 8
m = 5
y = 2009

if y <= 0:
    print("Date is invalid: year must be positive")

elif m < 1 or m > 12:
    print("Date is invalid: month must be between 1 and 12")

else:
    leap_year = (y % 4 == 0 and y % 100 != 0) or y % 400 == 0

if m in [1, 3, 5, 7, 8, 10, 12]:
    max_days = 31

elif m in [4, 6, 9, 11]:
    max_days = 30

else:
    if leap_year:
        max_days = 29
    else:
        max_days = 28

if d < 1 or d > max_days:
    print(f"Date is invalid: month {m} has only {max_days} days")
else:
    print(f"Day: {d}")
    print(f"Month: {m}")
    print(f"Year: {y}")
    print("Date is valid")