def largest_number(arr):
    if not arr:
        return None
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

arr = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
largest = largest_number(arr)
print(f"The largest number in the list is {largest}")
