def square_root_convergents():
    """
      1 + 1 / (1 + (n / d))
    = 1 + 1 / ((n + d) / d)
    = 1 + d / (n + d)
    = (2d + n) / (n + d)


    """

    numerator, denominator = 1, 1

    i = 0

    bigger_numerator_count = 0

    while i <= 1000:
        i += 1

        numerator, denominator = (2 * denominator) + numerator, numerator + denominator

        if len(str(numerator)) > len(str(denominator)):
            bigger_numerator_count += 1

    return bigger_numerator_count


print((square_root_convergents()))