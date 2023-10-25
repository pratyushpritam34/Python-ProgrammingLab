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
initial_value = float(input("Enter the initial value for the calculator: "))
calculator = Calculator(initial_value)

# Perform arithmetic operations
operation = input("Enter the operation (+, -, *, /): ")
operand = float(input("Enter the operand: "))

if operation == "+":
    result = calculator + operand
elif operation == "-":
    result = calculator - operand
elif operation == "*":
    result = calculator * operand
elif operation == "/":
    result = calculator / operand
else:
    result = "Invalid operation."

print(f"Result: {result}")
