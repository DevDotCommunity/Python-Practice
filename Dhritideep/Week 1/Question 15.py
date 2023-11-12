nums = []
print("Enter the size of list: ", end="")
tot = int(input())
print("Enter", tot, "Elements for the list: ", end="")
for i in range(tot):
    nums.append(int(input()))

sum = 0
count = 0
for i in range(tot):
    if nums[i]%2 == 0:
        sum = sum + nums[i]
        count = count+1

if count==0:
    print("\nEven number is not found in this list!")
else:
    print("\nSum of Even Numbers =", sum)
