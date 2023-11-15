
number = int(input("Enter a number: "))
square_root = int(number ** 0.5)
if square_root ** 2 == number:
    print(f"{number} is a perfect square.")
else:
    print(f"{number} is not a perfect square.")
