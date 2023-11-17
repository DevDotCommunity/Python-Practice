#Task: Write a Python program to implement the Newton-Raphson method for finding the square root of a number. (Math Functions)

def newton_raphson_sqrt(number, tolerance=1e-10, max_iterations=100):
    
    x_old = 1.0
    for i in range(max_iterations):
        x_new = 0.5 * (x_old + number / x_old)

        if abs(x_new - x_old) < tolerance:
            return x_new

        x_old = x_new

    return x_new

num = float(input("Enter a number to find the square root: "))

result = newton_raphson_sqrt(num)
print(f"The square root of {num} is approximately {result}")
