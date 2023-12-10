import sympy

def is_truncatable_prime(n):
    # Assume prime
    n_str = str(n)
    n_digits = len(n_str)

    if not sympy.isprime(n):
        return False

    # Check all truncations of n
    for i in range(1, n_digits):
        left_anchor_truncation = int(n_str[:i])
        right_anchor_truncation = int(n_str[i:])

        if not sympy.isprime(left_anchor_truncation):
            return False

        if not sympy.isprime(right_anchor_truncation):
            return False

    return True

def truncatable_primes():
    results = []

    i = 11 # Earliest possible truncatable prime; single digit primes not "truncatable"

    while len(results) != 11:
        if is_truncatable_prime(i):
            results.append(i)

        i += 1

    return sum(results)

print((truncatable_primes()))