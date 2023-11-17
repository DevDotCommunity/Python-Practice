#Task: Write a program to find the median of a list of numbers. (Lists, Sorting)

def find_median(numbers):
    sorted_numbers = sorted(numbers)

    middle_index = len(sorted_numbers) // 2

    if len(sorted_numbers) % 2 == 1:
        return sorted_numbers[middle_index]
    else:
        middle_values = sorted_numbers[middle_index - 1:middle_index + 1]
        return sum(middle_values) / 2

numbers = [4, 7, 1, 9, 2, 5, 8]
median = find_median(numbers)
print(f"The median is: {median}")
