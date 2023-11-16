#Task: Write a Python program to find the prime factors of a number. (Loops, Lists)

def prime_factors(num):
    factors = []
    divisor = 2

    while num > 1:
        while num % divisor == 0:
            factors.append(divisor)
            num //= divisor
        divisor += 1

    return factors

num = int(input("Enter a number: "))

result = prime_factors(num)
print(f"Prime factors of {num}: {result}")
