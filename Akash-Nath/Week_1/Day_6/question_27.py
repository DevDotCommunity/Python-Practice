#Task: Write a Python program to calculate the power of a number. (Math Functions)

from math import pow

baseNum = int(input("Enter the number: "))
power = int(input("Enter power: "))

print(f"{baseNum} to the power {power} is {pow(baseNum, power)}")