import math

def simple_sieve(limit):
    """
    Implementation of the simple sieve of Eratosthenes algorithm.
    """
    primes = []
    sieve = [True] * (limit + 1)
    for p in range(2, int(math.sqrt(limit)) + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
    return primes

def segmented_sieve(start, end):
    """
    Implementation of the segmented sieve algorithm.
    """
    limit = int(math.sqrt(end)) + 1
    primes = simple_sieve(limit)
    segmented_primes = []

    sieve = [True] * (end - start + 1)

    for p in primes:
        # Find the smallest multiple of the current prime number
        # that is greater than or equal to the start
        base = max(p * p, ((start + p - 1) // p) * p)
        
        # Mark all multiples of p within the range [start, end] as False
        for i in range(base, end + 1, p):
            sieve[i - start] = False

    # Add remaining primes within the range to the segmented_primes list
    for i in range(max(2, start), end + 1):
        if sieve[i - start]:
            segmented_primes.append(i)

    return segmented_primes

# Example usage:
start_range = 2
end_range = 5000
print("Prime numbers between", start_range, "and", end_range, "are:")
print(segmented_sieve(start_range, end_range))

