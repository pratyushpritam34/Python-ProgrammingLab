def delete_number_at_index(arr, index):
    if index < 0 or index >= len(arr):
        print("Invalid index")
    else:
        del arr[index]

arr = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
index = int(input(f"Enter the index (0 to {len(arr) - 1}) to delete the number: "))
delete_number_at_index(arr, index)
print("Updated list:", arr)
