import itertools
import collections
import math

def integer_right_triangles(max_perimeter: int):
    count_by_perimeter = collections.defaultdict(int)
    EPSILON = 1e-7  # Accepted error on hypotenuse calculation for determining if an integer

    for a, b in itertools.combinations_with_replacement(list(range(1, max_perimeter - 1)), 2):
        if a + b >= max_perimeter:
            continue

        c = math.sqrt(a ** 2 + b ** 2)

        if abs(c - round(c)) >= EPSILON:
            continue

        perimeter = a + b + round(c)

        if perimeter > max_perimeter:
            continue

        count_by_perimeter[perimeter] += 1

    max_perimeter, max_count = max(list(count_by_perimeter.items()), key=lambda x: x[1])

    return max_perimeter

print((integer_right_triangles(1000)))
