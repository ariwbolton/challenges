def coin_sums(denominations: [int], target: int, denomination_index=None, memo=None) -> int:
    if denomination_index is None:
        denomination_index = len(denominations) - 1

    if memo is None:
        memo = {}

    memo_key = (target, denomination_index)

    if memo_key in memo:
        return memo[memo_key]


    # Return the sum of either using one of the largest denomination, or permanently blocking using the largest denomination

    coin_sum = 0

    if target == 0:
        # If we've reached zero, this means we've found a unique coin sum
        coin_sum = 1
    else:
        if denomination_index > 0:
            # Stop using this denomination
            coin_sum += coin_sums(denominations, target, denomination_index - 1, memo)

        if target >= denominations[denomination_index]:
            # Use this denomination once
            coin_sum += coin_sums(denominations, target - denominations[denomination_index], denomination_index, memo)

    memo[memo_key] = coin_sum

    return coin_sum

print(coin_sums([1, 2, 5, 10, 20, 50, 100, 200], 200))
