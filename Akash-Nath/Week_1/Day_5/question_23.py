#Task: Write a Python program to check if a number is prime. (Loops, Conditional Statements)

# Input number
num = int(input("Enter a number: "))

if num <= 1:
    is_prime = False
elif num == 2:
    is_prime = True
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
