#Task: Write a program that converts a decimal number to a binary number. (Bitwise Operations)

decimal_num = int(input("Enter a decimal number: "))
binary_num = ""

while decimal_num > 0:
    binary_num = str(decimal_num % 2) + binary_num
    decimal_num //= 2

print(f"The binary representation is: {binary_num}")
