def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1
arr = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
target = int(input("Enter the element to search for: "))
index = linear_search(arr, target)
if index != -1:
    print(f"The element {target} was found at index {index}.")
else:
    print(f"The element {target} was not found in the list.")
