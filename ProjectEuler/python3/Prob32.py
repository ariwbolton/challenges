def pandigital_products():
    # Try all combinations of 2-digit and 3-digit numbers, and 1- and 4- digit numbers
    products = set()

    for i in range(10, 100):
        for j in range(100, 1000):
            if is_pandigital_combo(i, j, i * j):
                products.add(i * j)

    for i in range(1, 10):
        for j in range(1000, 10000):
            if is_pandigital_combo(i, j, i * j):
                products.add(i * j)

    return sum(products)

def is_pandigital_combo(a, b, c):
    s = str(a) + str(b) + str(c)

    return len(s) == 9 and len(set(s) - { '0' }) == 9

print(pandigital_products())