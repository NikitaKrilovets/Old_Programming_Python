first_number = float(input("Enter the first number: "))
operation = input("Enter the operation symbol: ")
second_number = float(input("Enter the second number: "))

if operation == "+":
    result = first_number + second_number
    print(f"{first_number} {operation} {second_number} = {result:.4f}")

elif operation == "-":
    result = first_number - second_number
    print(f"{first_number} {operation} {second_number} = {result:.4f}")

elif operation == "*":
    result = first_number * second_number
    print(f"{first_number} {operation} {second_number} = {result:.4f}")

elif operation == "/":
    if second_number == 0:
        print("Помилка: на нуль ділити не можна.")
    else:
        result = first_number / second_number
        print(f"{first_number} {operation} {second_number} = {result:.4f}")

elif operation == "//":
    if second_number == 0:
        print("Помилка: на нуль ділити не можна.")
    else:
        result = first_number // second_number
        print(f"{first_number} {operation} {second_number} = {result:.4f}")

elif operation == "%":
    if second_number == 0:
        print("Помилка: на нуль ділити не можна.")
    else:
        result = first_number % second_number
        print(f"{first_number} {operation} {second_number} = {result:.4f}")

elif operation == "**":
    result = first_number ** second_number
    print(f"{first_number} {operation} {second_number} = {result:.4f}")

else:
    print("Помилка: невідомий знак операції.")