#Task: Write a program to calculate the sum of squares of natural numbers up to a given limit. (Loops)

limit = int(input("Enter the integer limit: "))

sum = 0

for i in range(1, limit+1):
    sum += i**2
    
print(f"The sum of squares of natural numbers up to {limit} is {sum}")