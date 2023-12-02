import sympy


def get_all_rotations(n):
    n_str = str(n)

    return [int(n_str[i:] + n_str[:i]) for i in range(len(n_str))]

def circular_primes(up_to):
    results = set()

    for i in range(up_to + 1):
        if i not in results and sympy.isprime(i):
            rotations = get_all_rotations(i)
            if all(sympy.isprime(p) for p in rotations):
                for p in rotations:
                    results.add(p)

    return len(results)

print(circular_primes(10 ** 6))

