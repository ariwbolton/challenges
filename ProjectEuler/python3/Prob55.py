def lychrel_numbers(max_num):
    """Doesn't quite work; I'm off by a couple for some reason"""
    lychrel_count = 0
    lychrel_numbers = []

    for i in range(max_num):
        if is_lychrel(i):
            lychrel_count += 1
            lychrel_numbers.append(i)

    print(lychrel_numbers)

    return lychrel_count

def is_lychrel(n):
    is_lychrel = True

    for iteration in range(50):
        if n == int(str(n)[::-1]):
            is_lychrel = False
            break

        n = n + int(str(n)[::-1])

    return is_lychrel

print(lychrel_numbers(10_000))