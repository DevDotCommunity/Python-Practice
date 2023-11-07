#Task: Write a Python program to find the factors of a number. (Loops)

num = int(input("Enter a number: "))
factors = []

for i in range(1, num+1):
    if num % i == 0:
        factors.append(i)
print("The factors of", num, "are: ", end="")
print(*factors, sep=", ")
