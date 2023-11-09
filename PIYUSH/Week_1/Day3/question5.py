numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
even_sum = 0
for number in numbers:
    if number % 2 == 0:
        even_sum += number
print("Sum of even numbers:", even_sum)
#end of day3last task
