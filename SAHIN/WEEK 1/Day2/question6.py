#6. Write a Python program to find the largest among three numbers entered by the user. (Conditional Statements)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

largest = a

if b > largest:
  largest = b

if c > largest:
  largest = c

print("The largest number is", largest)
