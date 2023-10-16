def C_odd_numbers(arr):
    return [x for x in arr if x % 2 != 0]

arr = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
odd_numbers = C_odd_numbers(arr)
print("Odd numbers in the list:", odd_numbers)
