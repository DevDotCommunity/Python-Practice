#Task: Write a Python program to find the intersection of two lists. (Lists, Sets)

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

def find_common(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2:
            common_elements.append(element)
    return common_elements

result = find_common(list1, list2)
print(result)