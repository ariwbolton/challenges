import math

def digit_factorials():
    curious_numbers = []

    # Precompute, for speed
    factorials = { i: math.factorial(i) for i in range(0, 10)}

    # The max that any digit is worth is 9! = 362_880
    # 7 digits of 9 would only sum to 7 * 9! = 2_540_160
    # Use that as an upper bound to check (even though it certainly isn't a curious number itself)
    MAX_CURIOUS_NUMBER = 2_540_160

    # 1! and 2! are not allowed per the problem statement
    for i in range(3, MAX_CURIOUS_NUMBER + 1):
        if sum(factorials[int(d)] for d in str(i)) == i:
            curious_numbers.append(i)

    return sum(curious_numbers)

print((digit_factorials()))