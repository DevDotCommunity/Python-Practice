#Task: Write a Python program to find the maximum product of two integers in an array. (Lists)

inp_list = [42, 17, 8, 29, 54, 10, 33, 21, 7, 91]
max_product = 0

for i in range(len(inp_list)):
    for j in range(i+1, len(inp_list)):
        product = inp_list[i] * inp_list[j]
        if product > max_product:   
            max_product = product
            
print(max_product)