#Task: Write a program to find the average of a list of numbers. (Lists)

def average(list_of_numbers):
    result = 0
    for number in list_of_numbers:
        result += number
    
    average = result/len(list_of_numbers)
    
    return average

list_of_numbers = [1, 2, 3, 4, 5]
print(average(list_of_numbers))