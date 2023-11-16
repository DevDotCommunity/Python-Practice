#Task: Write a Python program to implement a basic calculator that can perform addition, subtraction, multiplication, and division. (Conditional Statements)

def calculations(num1, num2, operation):
    if operation == "+":
        return num1+num2
    elif operation == "-":
        return num1-num2
    elif operation == "*":
        return num1*num2
    elif operation == "/":
        return num1/num2
    
while True:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Enter the operation you want to perform[+|-|*|/]: ")

    print(f"The result is: {calculations(num1, num2, operation)}")