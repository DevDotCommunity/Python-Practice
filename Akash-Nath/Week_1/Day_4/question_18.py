#Task: Write a program to generate the Fibonacci sequence up to n terms. (Lists, Loops)

n = int(input("Enter the number of terms: "))

n1, n2 = 0, 1

count = 0

if n <= 0:
    print("Please enter a positive integer")
    
elif n == 1:
    print("Fibonacci sequence upto", n, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(n1)
        nth = n1 + n2
        
        n1 = n2
        n2 = nth
        count += 1