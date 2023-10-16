def num_zero(n):
    if n < 0:
        return
    print(n)
    num_zero(n - 1)
n = int(input("Enter a number (n): "))
num_zero(n)
