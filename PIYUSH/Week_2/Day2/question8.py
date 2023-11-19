
limit = int(input("Enter the limit: "))
sum_of_squares = sum(i**2 for i in range(1, limit + 1))
print(f"The sum of squares of natural numbers up to {limit} is: {sum_of_squares}")
