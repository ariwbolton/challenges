import sympy


def side_length(layer):
    return (2 * layer) - 1  # 2nd layer -> 3, 3rd layer -> 5, ...


def diagonal_numbers_for_layer(layer):
    current_side_length = side_length(layer)
    lower_right_number = current_side_length ** 2

    return [lower_right_number - (i * (current_side_length - 1)) for i in range(0, 4)]


def total_diagonals_for_layer(layer):
    return (2 * side_length(layer)) - 1


def spiral_primes():
    layer = 2
    primes_on_diagonals = 3

    while primes_on_diagonals / total_diagonals_for_layer(layer) >= 0.1:
        print((layer, primes_on_diagonals, total_diagonals_for_layer(layer), primes_on_diagonals / total_diagonals_for_layer(layer)))

        layer += 1

        for n in diagonal_numbers_for_layer(layer):
            if sympy.isprime(n):
                primes_on_diagonals += 1

    print((layer, primes_on_diagonals, total_diagonals_for_layer(layer), primes_on_diagonals / total_diagonals_for_layer(layer)))

    return side_length(layer)


print((spiral_primes()))
