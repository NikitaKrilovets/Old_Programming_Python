name = "Nikita"
surname = "Krilovets"
group = "IT-31"

d = 8
c = 9

print(f"{name} {surname}, {group}")

count = 0
sum_numbers = 0
product = 1
even = 0
odd = 0

print(f"Numbers from {d} to 31:", end=" ")

for i in range(d, 32):
    print(i, end=" ")

    count += 1
    sum_numbers += i
    product *= i

    if i % 2 == 0:
        even += 1
    else:
        odd += 1

average = sum_numbers / count

print()
print(f"Count: {count}")
print(f"Sum: {sum_numbers}")
print(f"Product: {product}")
print(f"Average: {average:.2f}")
print(f"Even: {even}, odd: {odd}")


# while version

count = 0
sum_numbers = 0
product = 1
even = 0
odd = 0

i = d

print(f"\nNumbers from {d} to 31:", end=" ")

while i <= 31:
    print(i, end=" ")

    count += 1
    sum_numbers += i
    product *= i

    if i % 2 == 0:
        even += 1
    else:
        odd += 1

    i += 1

average = sum_numbers / count

print()
print(f"Count: {count}")
print(f"Sum: {sum_numbers}")
print(f"Product: {product}")
print(f"Average: {average:.2f}")
print(f"Even: {even}, odd: {odd}")


print("\nCountdown:", end=" ")

for i in range(c, 0, -1):
    print(i, end=" ")

print()