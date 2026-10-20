name = "Nikita"
surname = "Krilovets"
group = "IT-31"

d = 8
c = 9

n = d * c

print(f"{name} {surname}, {group}")
print(f"n = {d} * {c} = {n}")


# Divisors

count = 0
sum_divisors = 0

print("Divisors:", end=" ")

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
        count += 1
        sum_divisors += i

print()
print(f"Divisors count: {count}, sum: {sum_divisors}")


# Check if n is prime

for i in range(2, n):
    if n % i == 0:
        print(f"{n} is not prime")
        break
else:
    print(f"{n} is prime")


# All prime numbers from 2 to n

primes_count = 0

print(f"Primes up to {n}:", end=" ")

for number in range(2, n + 1):
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        print(number, end=" ")
        primes_count += 1

print()
print(f"Primes count: {primes_count}")