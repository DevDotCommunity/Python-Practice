#Task: Write a Python program to find the largest among three numbers entered by the user. (Conditional Statements)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2:
    if num1 > num3:
        print(f"{num1} is the largest number.")
    else:
        print(f"{num3} is the largest number.")
else:
    if num2 > num3:
        print(f"{num2} is the largest number.")
    else:
        print(f"{num3} is the largest number.")