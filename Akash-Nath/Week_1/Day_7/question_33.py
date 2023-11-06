#Task: Write a program to calculate the sum of the digits of a number. (Loops, Basic Arithmetic)

num = input("Enter a number: ")
digits = []

for i in num:
    digits.append(int(i))
    
print(f"Sum of digits of {num} is {sum(digits)}")