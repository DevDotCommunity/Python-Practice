#Task: Write a program to find the smallest element in a list. (Lists, Loops)

my_list = [5, 3, 8, 1, 9, 2]

smallest = my_list[0] # initialize the smallest element to the first element of the list

# loop through the list and compare each element to the current smallest
for element in my_list:
    if element < smallest:
        smallest = element

print("The smallest element in the list is:", smallest)

