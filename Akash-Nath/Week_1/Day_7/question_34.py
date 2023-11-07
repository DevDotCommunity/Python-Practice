#Task: Write a Python program to check if a number is a perfect square. (Math Functions)

import math

num = int(input("Enter a number: "))

if math.sqrt(num) == int(math.sqrt(num)):
    print(f"{num} is a perfect square")
else:
    print(f"{num} is not a perfect square")