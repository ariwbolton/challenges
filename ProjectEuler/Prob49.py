import util
from collections import defaultdict, Counter
from itertools import combinations

import string

def digit_decomposition(n):
    digit_counter = Counter(str(n))

    return tuple(digit_counter[d] for d in string.digits)

def prime_permutations():
    primes_4_digit = [p for p in util.sieve((10 ** 4) - 1) if p >= 10 ** 3]

    prime_digit_decomposition_map = defaultdict(list)

    for prime in primes_4_digit:
        prime_digit_decomposition_map[digit_decomposition(prime)].append(prime)

    for decomposition, primes in list(prime_digit_decomposition_map.items()):
        if len(primes) < 3:
            continue

        sorted_primes = sorted(primes)

        for (p1, p2, p3) in combinations(sorted_primes, 3):
            if (p2 - p1) == (p3 - p2):
                print((p1, p2, p3))

prime_permutations()