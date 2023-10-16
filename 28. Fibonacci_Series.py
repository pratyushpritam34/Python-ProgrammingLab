def fibonacci_Series(n):
    fibona_series = [0, 1]
    for i in range(2, n):
        next_term = fibona_series[-1] + fibona_series[-2]
        fibona_series.append(next_term)
    return fibona_series

n = int(input("Enter the number of terms in the Fibonacci series: "))
fibona_series = fibonacci_Series(n)
print("Fibonacci series:", fibona_series)
