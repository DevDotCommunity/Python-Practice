num = int(input("Enter a number: "))
f = 1
i = 1
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    while i <= num:
        f *= i
        i += 1

    # Display the result
    print(f"The factorial of {num} is {f}")
#end of task4
