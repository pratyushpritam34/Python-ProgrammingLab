import cmath
def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 = (-b - cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b + cmath.sqrt(discriminant)) / (2*a)
    return root1, root2
a = float(input("Enter the coefficient 'a': "))
b = float(input("Enter the coefficient 'b': "))
c = float(input("Enter the coefficient 'c': "))
root1, root2 = quadratic_roots(a, b, c)
print(f"Root 1: {root1}, Root 2: {root2}")
