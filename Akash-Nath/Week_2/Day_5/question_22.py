#Task: Write a program to find the mode of a list of numbers. (Lists)

import statistics

input_numbers = input("Enter a list of numbers separated by spaces: ")
numbers = [float(x) for x in input_numbers.split()]

try:
    mode = statistics.mode(numbers)
    print(f"Mode of the list: {mode}")
except statistics.StatisticsError:
    print("There is no unique mode in the list.")
