def sum_of_numbers(numbers):
    return sum(numbers)

n = int(input("Enter the number of elements: "))
numbers = [float(input(f"Enter number {i+1}: ")) for i in range(n)]
result = sum_of_numbers(numbers)
print(f"The sum of the numbers is {result}")
