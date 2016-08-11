import time
import math

# return array of primes up to and including n
def sieve(n):
    starttime = time.clock()
    array = [1] * (n + 1)

    for i in xrange(2, int(math.sqrt(n)) + 1):
        if array[i]:
            for j in xrange(2, (n / i) + 1):
                array[i * j] = 0

    primes = list()

    for i in xrange(2, len(array)):
        if array[i]:
            primes.append(i)


    endtime = time.clock()
    print "Took %f seconds" % (endtime - starttime)
    return primes

primes = sieve(100)

# memoization table
storedPairs = dict()

