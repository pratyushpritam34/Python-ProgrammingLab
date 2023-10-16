def fibonacci_S_R(n):
    if n <= 1:
        return n
    else:
        return fibonacci_S_R(n - 1) + fibonacci_S_R(n - 2)

n = int(input("Enter the value of N: "))
result = fibonacci_S_R(n)
print(f"The {n}th term in the Fibonacci series is {result}")
