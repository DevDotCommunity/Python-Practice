limit = int(input("Enter the limit: "))
sum = 0

for number in range(2, limit + 1):
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
       sum += number

print(f"The sum of prime numbers up to {limit} is: {prime_sum}")
