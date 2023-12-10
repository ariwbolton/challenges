def pandigital_multiples():
    # Rough back of the napkin math shows that these limits hold
    MAX_NUM_BY_VECTOR_LENGTH = {
        2: 10 ** 5,
        3: 10 ** 3,
        4: 10 ** 3,
        5: 10 ** 2,
        6: 10 ** 2,
        7: 10 ** 2
    }
    max_pandigital = 0

    for vector_length in range(2, 8):
        for i in range(1, MAX_NUM_BY_VECTOR_LENGTH[vector_length]):
            products = tuple(i * mult for mult in range(1, vector_length + 1))

            if is_pandigital_combo(*products):
                pandigital = int(''.join(str(n) for n in products))

                max_pandigital = max(max_pandigital, pandigital)

    return max_pandigital

def is_pandigital_combo(*nums: [int]):
    s = ''.join(str(n) for n in nums)

    return len(s) == 9 and len(set(s) - {'0'}) == 9

print((pandigital_multiples()))
