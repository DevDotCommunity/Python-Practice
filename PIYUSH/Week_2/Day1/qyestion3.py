# Input two lists
list1 = input("Enter elements of the first list separated by spaces: ").split()
list2 = input("Enter elements of the second list separated by spaces: ").split()

# Convert input strings to lists of integers
list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]

# Find the intersection without using library functions
intersection = [value for value in list1 if value in list2]

# Print the intersection
print(f"The intersection of the two lists is: {intersection}")
