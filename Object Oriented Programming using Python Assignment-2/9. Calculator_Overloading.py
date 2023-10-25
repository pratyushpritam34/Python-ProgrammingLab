class Calculator:
    def __init__(self, value):
        self.value = value

    def add(self, other):
        return self.value + other

    def subtract(self, other):
        return self.value - other

    def multiply(self, other):
        return self.value * other

    def divide(self, other):
        if other == 0:
            return "Division by zero is not allowed"
        return self.value / other

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

    def __mul__(self, other):
        return self.multiply(other)

    def __truediv__(self, other):
        return self.divide(other)
calculator = Calculator(199)
result1 = calculator + 36
result2 = calculator - 61
result3 = calculator * 25
result4 = calculator / 17

print("Addition:", result1)
print("Subtraction:", result2)
print("Multiplication:", result3)
print("Division:", result4)
