def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num //= 10
    return total
num = int(input("Enter an integer: "))
sum = sum_of_digits(num)
print(f"The sum of the digits is {sum}")
