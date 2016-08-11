import math

def sieve(n):
	# compute boolean array of primes up to and including n
    array = [1] * (n + 1)

    for i in xrange(2, int(math.sqrt(n)) + 1):
        if array[i]:
            for j in xrange(2, (n / i) + 1):
                array[i * j] = 0
    return array
