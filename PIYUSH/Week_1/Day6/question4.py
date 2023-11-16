
numbers = [int(x) for x in input("Enter the array elements separated by space: ").split()]
s
max_value = float('-inf')
second_max_value = float('-inf')

# Iterate through the array to find the maximum and second maximum values
for num in numbers:
    if num > max_value:
        second_max_value = max_value
        max_value = num
    elif num > second_max_value:
        second_max_value = num

# Calculate the maximum product
max_product = max_value * second_max_value

# Print the result
print("Maximum product of two integers:", max_product)
