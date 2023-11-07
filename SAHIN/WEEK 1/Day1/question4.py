# 4. Write a Python program to calculate the factorial of a number. (Loops)

# def factorial(n):
#   if n == 0:
#     return 1
#   else:
#     return n * factorial(n - 1)

# number = int(input("Enter a number: "))
# print("The factorial of", number, "is", factorial(number))
def factorial(n):
  result = 1

  for i in range(1, n + 1):
    result = result * i  
  return result

n = int(input("Enter a number: "))
print("The factorial of", n, "is", factorial(n))
