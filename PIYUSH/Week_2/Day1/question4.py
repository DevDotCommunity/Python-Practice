# Input list and the number of positions to rotate
original_list = input("Enter elements of the list separated by spaces: ").split()
rotate_by = int(input("Enter the number of positions to rotate to the left: "))

# Convert input strings to a list of integers
original_list = [int(x) for x in original_list]

# Calculate the new rotated list
rotated_list = original_list[rotate_by % len(original_list):] + original_list[:rotate_by % len(original_list)]

# Print the rotated list
print(f"The original list: {original_list}")
print(f"The list after rotating to the left by {rotate_by} positions: {rotated_list}")
