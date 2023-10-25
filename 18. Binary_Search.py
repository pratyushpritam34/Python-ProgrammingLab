def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Target found, return its index
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found

# User input to create a sorted list
input_numbers = input("Enter a sorted list of numbers separated by spaces: ")
numbers = [int(num) for num in input_numbers.split()]

target = int(input("Enter the target number to search for: "))

# Perform binary search
result = binary_search(numbers, target)

if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the list.")

