import copy

import util

def longest_prime_sum(n):
    primes = util.sieve(n)

    prime_set = set(primes)

    # Find "max length of sequence" by iterating from first prime
    # Probably unnecessary; seems like these sequences generally start from a number less than 20 or so, so there's not much to search through
    sequence_from_1_total = 0
    sequence_from_1_count = 0

    for prime in primes:
        if sequence_from_1_total >= n:
            break

        sequence_from_1_total += prime
        sequence_from_1_count += 1

    max_length = 0
    max_length_prime = None
    max_length_seq = None
    i = 0

    # No need to check past half of `n` b/c any pair of primes above those values will be greater than `n`, and we know the longest seq is > 2
    # This is a very conservative upper bound; it's certainly much lower
    while i < len(primes) and primes[i] < n // 2:
        sequence_from_i_total = 0
        sequence_from_i_count = 0
        seq = []

        for j in range(0, sequence_from_1_count):
            sequence_from_i_total += primes[i + j]
            sequence_from_i_count += 1
            seq.append(primes[i + j])

            if sequence_from_i_total > n:
                break

            if sequence_from_i_total in prime_set and sequence_from_i_count > max_length:
                max_length = sequence_from_i_count
                max_length_prime = sequence_from_i_total
                max_length_seq = copy.copy(seq)

        i += 1

    return max_length_prime

print('result', longest_prime_sum(1000000))

