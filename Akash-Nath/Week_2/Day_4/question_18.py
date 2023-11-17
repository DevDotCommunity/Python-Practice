#Task: Write a program to check if a list is sorted in ascending order. (Lists)

def is_sorted(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True

list = [1, 2, 3, 4, 5]
print(is_sorted(list))