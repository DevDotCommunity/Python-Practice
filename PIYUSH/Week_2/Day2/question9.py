
set1 = set(input("Enter elements of the first set separated by spaces: ").split())
set2 = set(input("Enter elements of the second set separated by spaces: ").split())


union_set = set1.union(set2)


print(f"The union of the two sets is: {union_set}")
