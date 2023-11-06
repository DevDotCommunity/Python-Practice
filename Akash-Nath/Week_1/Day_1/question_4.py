#Task: Write a Python program to calculate the factorial of a number. (Loops)

num = int(input("Enter the number you want the factorial upto: "))

result = 1

for i in range(1, num+1):
    result *= i
    i += 1
    
print(result)