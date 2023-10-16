def product_of_numbers(numbers):
    result = 1  
    for number in numbers:
        result *= number 
    return result
numbers = [float(x) for x in input("Enter a list of real numbers separated by spaces: ").split()]
result = product_of_numbers(numbers)
print(f"The product of the numbers is: {result}")
