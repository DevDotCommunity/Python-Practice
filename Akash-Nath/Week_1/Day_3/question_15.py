#Task: Write a program to find the sum of all even numbers in a list. (Lists, Loops)

lst = [4, 2, 6, 0, 9, 7, 1, 3, 5, 8]

sum = 0

for item in lst:
    if item % 2 == 0:
        sum += item
    else:
        continue

print(f"The sum of all even numbers in given list is {sum}")