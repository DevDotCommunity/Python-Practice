# 4. Write a Python program to calculate the factorial of a number. (Loops)

# def factorial(n):
#   if n == 0:
#     return 1
#   else:
#     return n * factorial(n - 1)

# number = int(input("Enter a number: "))
# print("The factorial of", number, "is", factorial(number))

n = int (input ("Enter a number: "))

if n >= 1:
    for i in range (1, n+1):

print("Factorial of the given number is: ", i)