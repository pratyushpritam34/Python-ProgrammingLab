def reverse_integer(number):
    reversed_str = str(number)[::-1]
    reversed_number = int(reversed_str)
    return reversed_number
number = int(input("Enter an integer: "))
reversed_number = reverse_integer(number)
print(f"The reversed integer is: {reversed_number}")
