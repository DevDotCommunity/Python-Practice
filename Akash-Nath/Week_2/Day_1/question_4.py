#Task: Write a program to rotate the elements of a list to the left by a specific number of positions. (Lists)

def rotate_left(lst, positions):
    positions = positions % len(lst)
    return lst[positions:] + lst[:positions]

user_list = [1, 2, 3, 4, 5]
user_positions = int(input("Enter the number of positions to rotate left: "))

result = rotate_left(user_list, user_positions)
print(f"The list after rotating {user_positions} positions to the left is: {result}")
