#Task: Write a program to find the missing number in a list of integers from 1 to n. (Lists)

def find_missing_number(nums, n):
    expected_sum = n * (n + 1) // 2

    actual_sum = sum(nums)

    missing_number = expected_sum - actual_sum

    return missing_number

num_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
n = int(input("Enter the value of n: "))

result = find_missing_number(num_list, n)
print(f"The missing number is: {result}")
