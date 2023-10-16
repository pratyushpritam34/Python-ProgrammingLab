def insert_number_at_position(arr, num, position):
    if position < 0 or position > len(arr):
        print("Invalid position")
    else:
        arr.insert(position, num)

arr = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
num = int(input("Enter the number to insert: "))
position = int(input(f"Enter the position (0 to {len(arr)}) to insert the number: "))
insert_number_at_position(arr, num, position)
print("Updated list:", arr)
