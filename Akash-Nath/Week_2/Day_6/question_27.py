#Task: Write a program that calculates the square of each element in a list. (Lists)

def calculate(lst):
    for element in lst:
        print(element**2)

lst = [1,2,3,4,5,6,7,8,9,10]
calculate(lst)