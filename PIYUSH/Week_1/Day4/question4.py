import math

def find_lcm(a, b):
    if a == 0 or b == 0:
        return 0  # LCM of 0 and any number is 0
    else:
        return abs(a * b) // math.gcd(a, b)

# Input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm = find_lcm(num1, num2)

print(f"The LCM of {num1} and {num2} is {lcm}")
#end of question4
