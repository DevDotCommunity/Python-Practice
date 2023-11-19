number = int(input("Enter a number: "))
print(f"Prime factors of {number} are: ", end="")

divisor = 2

while number > 1:
    if number % divisor == 0:
        print(divisor, end=" ")
        number //= divisor
    else:
        divisor += 1

print()
//end of day5 p1
