#Task: Write a Python program to find the GCD (Greatest Common Divisor) of two numbers. (Math Functions)

from math import gcd

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"The GCD of {num1} and {num2} is {gcd(num1, num2)}")