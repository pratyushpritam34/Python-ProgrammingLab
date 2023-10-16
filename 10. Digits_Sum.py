
print("Integers within the range 100 to 200 with an even sum of digits:")
for number in range(100, 201):
    digits = [int(digit) for digit in str(number)]
    digit_sum = sum(digits)
    if digit_sum % 2 == 0:
        print(number)
