
number = int(input("Enter a number: "))
sum_of_digits = 0
while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number //= 10
print("The sum of the digits is:", sum_of_digits)
