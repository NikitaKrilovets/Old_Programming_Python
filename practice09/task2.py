name = "Nikita"
surname = "Krilovets"
group = "IT-31"

print(f"{name} {surname}, {group}")

number = int(input("Enter an integer: "))

if number <= 0:
    print("The number must be positive")
else:
    temp = number

    digits = 0
    sum_digits = 0
    max_digit = 0
    min_digit = 9
    reversed_number = 0

    while temp > 0:
        digit = temp % 10

        digits += 1
        sum_digits += digit

        if digit > max_digit:
            max_digit = digit

        if digit < min_digit:
            min_digit = digit

        reversed_number = reversed_number * 10 + digit

        temp = temp // 10

    print(f"Digits: {digits}")
    print(f"Sum of digits: {sum_digits}")
    print(f"Max digit: {max_digit}, min digit: {min_digit}")
    print(f"Reversed: {reversed_number}")