#Task: Write a Python program to find the n-th term in the Fibonacci sequence using recursion. (Recursion)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Enter the number: "))
if n <= 0:
    print("Please enter a positive integer")
else:
    print(f"The {n}th term in the Fibonacci sequence is {fibonacci(n)}")