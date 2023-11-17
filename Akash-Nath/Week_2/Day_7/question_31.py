#Task:  Write a Python program to find the sum of all elements in a 2D list. (Lists)

def find_sum(lst):
    result = 0
    for element in lst:
        result += element
    return result

lst = [1, 2, 3, 4, 5, 6]

print(find_sum(lst))