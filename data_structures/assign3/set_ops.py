list1 = list(map(int, input("Enter numbers for first list: ").split()))
list2 = list(map(int, input("Enter numbers for second list: ").split()))

common_elements = set(list1) & set(list2)

print("Common elements:", list(common_elements))