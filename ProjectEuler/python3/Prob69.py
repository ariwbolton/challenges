import sympy

def totient_maximum(up_to):
    max_quotient = 0
    max_quotient_n = None

    for i in range(1, up_to + 1):
        quotient = i / sympy.totient(i)
        if quotient > max_quotient:
            max_quotient = quotient
            max_quotient_n = i

    return max_quotient_n

print(totient_maximum(10 ** 6))