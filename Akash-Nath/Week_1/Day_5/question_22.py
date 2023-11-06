#Task: Write a program to find the second largest element in an array. (Lists)

numbers = [12, 35, 1, 10, 34, 1]

if len(numbers) < 2:
    print("The list doesn't have a second largest number.")
else:
    largest = second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        print("There is no second largest number.")
    else:
        print("The second largest number is:", second_largest)
