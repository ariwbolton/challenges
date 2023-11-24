"""Solves Riddler Express, 1/11/19

Link `here <https://fivethirtyeight.com/features/in-space-no-one-can-hear-your-3d-printer-die/?ex_cid=story-twitter>`_
"""

import copy
# import primefac

from sympy.ntheory import factorint

# 530,131,801,762,787,739,802,889,792,754,109,70_,139,358,547,710,066,257,652,050,346,294,484,433,323,974,747,960,297,803,292,989,236,183,040,000,000,000

def main():
    """Entry point"""
    factors_of_2_5 = {}
    has_2_or_5 = set()
    has_2 = set()
    has_5 = set()
    no_2_or_5 = set()

    for i in range(1, 100):
        two_factors, five_factors = get_10_factors(i)

        factors_of_2_5[i] = {
            2: two_factors,
            5: five_factors
        }

        if factors_of_2_5[i][2] or factors_of_2_5[i][5]:
            has_2_or_5.add(i)

            if factors_of_2_5[i][2]:
                has_2.add(i)
            else:
                has_5.add(i)
        else:
            no_2_or_5.add(i)

    # Minimum number of twos and fives needed
    # If we have more twos than the number here, we must have exactly this number of fives
    # If we have more fives than the number here, we must have exactly this number of twos
    exact_factors = {
        2: 17,
        5: 10
    }

    exact_factors = {
        2: 5,
        5: 3
    }

    finished_set, unfinished_set = generate_possibilities(factors_of_2_5, copy.deepcopy(factors_of_2_5), exact_factors, 1, 20)

    import pdb; pdb.set_trace()


def get_10_factors(n):
    """Determine the number of times 2 and 5 go into ``n``"""
    return multiplicity(n, 2), multiplicity(n, 5)


def multiplicity(n, d):
    """Given ``n``, determine the number of times d divides it"""
    total, v = 0, n

    while v % d == 0:
        total += 1
        v = v // d

    return total


def generate_possibilities(small_factors, all_factors, factors_limits_dict, current_number, last_number):
    """Return a 2-tuple, set of "completed selections", and set of "uncompleted selections". """
    if current_number > last_number:
        return set(), set()

    current_num_factors = small_factors[current_number]

    if current_number == last_number:
        # Handle base case
        return set(), {current_number, 1}

    finished_set, uncompleted_set = generate_possibilities(small_factors, all_factors, factors_limits_dict, current_number + 1, last_number)

    new_finished_set = set()
    new_uncompleted_set = set()

    for res in uncompleted_set:
        res_factors = all_factors[res]

        can_add, finished, result_factors = can_add_number(current_num_factors, res_factors, factors_limits_dict)

        if can_add:
            new_num = res * current_number

            if finished:
                new_finished_set.add(new_num)
            else:
                new_uncompleted_set.add(new_num)

            all_factors[new_num] = result_factors

    finished_set.update(new_finished_set)
    uncompleted_set.update(new_uncompleted_set)

    print("Finished {} | {} | {}".format(current_number, len(finished_set), len(uncompleted_set)))

    return finished_set, uncompleted_set


def can_add_number(current_num_factors, res_factors, factors_limits_dict):
    """Check if current_num_factors + res_factors <= factors_limits_dict, return appropriate info"""
    new_dict = {}
    finished = True

    for factor, current_amount in current_num_factors.items():
        result_factor_amount = res_factors[factor]
        factors_limit_amount = factors_limits_dict[factor]

        new_amount = current_amount + result_factor_amount

        if new_amount > factors_limit_amount:
            return False, None, None
        elif new_amount == factors_limit_amount:
            pass
        else:
            finished = False

        new_dict[factor] = new_amount

    return True, finished, new_dict

def test_sympy():
    s = '530,131,801,762,787,739,802,889,792,754,109,70{},139,358,547,710,066,257,652,050,346,294,484,433,323,974,747,960,297,803,292,989,236,183,040,000,000,000'

    original = {
        2: 17, 5: 10
    }

    for i in range(0, 1):
        s_i = s.format(i)
        num_i = int(s_i.replace(',', ''))

        import pdb; pdb.set_trace()

        num_i = num_i // (2 ** 17)
        num_i = num_i // (5 ** 10)

        factorization = factorint(num_i)

        if 2 not in factorization:
            factorization[2] = 0

        if 5 not in factorization:
            factorization[5] = 0

        factorization[2] += original[2]
        factorization[5] += original[5]

        print("For {} | {}".format(i, factorization))

def test_sympy_2():
    s = '530,131,801,762,787,739,802,889,792,754,109,700,139,358,547,710,066,257,652,050,346,294,484,433,323,974,747,960,297,803,292,989,236,183,040,000,000,000'

    n = int(s.replace(',', ''))

    n = n / (2 ** 17)
    n = n / (5 ** 10)

    print("For {} | {}".format(0, factorint(n)))

def other_test():
    s = '530,131,801,762,787,739,802,889,792,754,109,70{},139,358,547,710,066,257,652,050,346,294,484,433,323,974,747,960,297,803,292,989,236,183,040,000,000,000'

    for i in range(0, 10):
        s_i = s.format(i)
        num_i = int(s_i.replace(',', ''))

        success = max_factor_under_100(num_i)

        print("For {} | {}".format(i, success))

def max_factor_under_100(num_i):
    current_val = num_i

    for factor in range(2, 100):
        while current_val % factor == 0 and current_val != 1:
            current_val = current_val // factor

    print("Final val:", current_val)

    return current_val == 1


if __name__ == '__main__':
    other_test()
