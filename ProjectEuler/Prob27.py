import math
import time

def sieve(n):
    starttime = time.clock()
    array = [1] * (n + 1)

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i]:
            for j in range(2, (n / i) + 1):
                array[i * j] = 0

                   

    endtime = time.clock()
    print("Took %f seconds" % (endtime - starttime))
    return array


def generatePrimes(a, b, maxa, maxb, numprimes, primes):
    n = 0
    if not b in primes:
        return
    
    num = (n * n) + (a * n) + b
    
    while num in primes:
        n += 1
        num = (n * n) + (a * n) + b

    if n > numprimes:
        maxa = a
        maxb = b
        numprimes = n

def runProg():
    primes = sieve(1000000)

    maxa = 0
    maxb = 0
    numprimes = 0

    
    for a in range(-1000, 999):
        print(a)
        for b in range(999):
            generatePrimes(a, b, maxa, maxb, numprimes, primes)

    print(str(maxa) + " " + str(maxb) + " " + str(numprimes))
    print(maxa * maxb)

runProg()
        
