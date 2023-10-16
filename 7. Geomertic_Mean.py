import math
def geometric_mean(numbers):
    product = 1
    n = len(numbers)  
    for num in numbers:
        product *= num  
    geometric_mean = math.pow(product, 1/n)
    return geometric_mean
numbers = [float(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
result = geometric_mean(numbers)
print(f"The geometric mean of the numbers is {result}")
