def sieve_of_eratosthenes(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p] == True:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    primes = []
    for p in range(2, n + 1):
        if prime[p]:
            primes.append(p)
    return primes


# factorize a number (followed by finding prime numbers)
def factorize(n, primes):
    factors = []
    for prime in primes:
        while n % prime == 0:
            factors.append(prime)
            n //= prime
        if n == 1:
            break
    if n > 1:  # If n is still greater than 1, it's a prime number itself
        factors.append(n)
    return factors
