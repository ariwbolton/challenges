import math

def sieve(n):
    prime_bitmap = [1] * (n + 1)

    for i in range(2, int(math.sqrt(n)) + 1):
        if prime_bitmap[i]:
            for j in range(2, (n // i) + 1):
                prime_bitmap[i * j] = 0

    return [i for i, is_prime in enumerate(prime_bitmap) if is_prime and i >= 2]