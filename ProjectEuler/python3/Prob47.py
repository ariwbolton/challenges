import sympy
import collections

def distinct_prime_factors(seq_length, num_factors):
    factorizations = collections.deque()
    i = 1

    while (
        not (
            len(factorizations) == seq_length and
            all(len(f) == num_factors for f in factorizations)
        )
    ):
        factorizations.append(sympy.primefactors(i))

        if len(factorizations) > seq_length:
            factorizations.popleft()

        i += 1

    return i - seq_length

print(distinct_prime_factors(4, 4))