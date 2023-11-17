#Task: Write a program that removes duplicates from a list without using built-in functions. (Lists)

def remove_duplicates(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    return unique
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
unique = remove_duplicates(numbers)
print(unique)