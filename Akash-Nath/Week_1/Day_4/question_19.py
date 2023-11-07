#Task: Write a Python program to find the LCM (Least Common Multiple) of two numbers. (Math Functions)

from math import lcm

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"The LCM of the number {num1} and {num2} is {lcm(num1, num2)}")