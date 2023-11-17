#Task: Write a program to calculate the sum of all prime numbers up to a given limit. (Loops, Conditional Statements)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def sum_of_primes_up_to_limit(limit):
    prime_sum = 0
    for num in range(2, limit + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum

user_inp = int(input("Enter a limit: "))
result = sum_of_primes_up_to_limit(user_inp)
print(f"The sum of prime numbers up to {user_inp} is: {result}")
