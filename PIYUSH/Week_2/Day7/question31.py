
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
matrix = []
for i in range(rows):
    row = []
    for j in range(columns):
        element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(element)
    matrix.append(row)
total_sum = 0
for row in matrix:
    for element in row:
        total_sum += element
print(f"The sum of all elements in the 2D list is: {total_sum}")
