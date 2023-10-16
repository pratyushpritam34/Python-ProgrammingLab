def generate_primes(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % p != 0 for p in primes):
            primes.append(num)
    return primes

n = int(input("Enter a positive integer (N): "))
prime_numbers = generate_primes(n)
print(f"Prime numbers from 1 to {n}: {prime_numbers}")
