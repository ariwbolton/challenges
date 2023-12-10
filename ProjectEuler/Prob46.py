import math
import time

def sieve(n):
    starttime = time.clock()
    array = [1] * (n + 1)

    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i]:
            for j in range(2, (n / i) + 1):
                array[i * j] = 0

                   

    """          
    for i in xrange(2, n):
        if array[i]:
            print i
    """
    endtime = time.clock()
    print("Took %f seconds" % (endtime - starttime))
    return array

def prob(k, n):
    starttime = time.clock()
    sieveList = sieve(n)
    primes = []
    composites = []
    squares = list(map(lambda x, y: x * y, list(range(k)), list(range(k))))

    for i in range(n + 1):
        if sieveList[i]:
            primes.append(i)
        else:
            composites.append(i)

    #print primes
    #print composites

    oddComposites = [x for x in composites if x % 2]

    print(len(oddComposites))


    for num in range(1, len(oddComposites)):
        found = 0
        #if num % 10 == 0:
            #print num
            
        for i in range(1, k):
            if (2*squares[i]) > oddComposites[num]: break
            for j in range(1, len(primes)):
                if primes[j] > oddComposites[num]: break
                
                if oddComposites[num] == (primes[j] + (2 * squares[i])):
                    #print str(oddComposites[num]) + " = " + str(primes[j]) + " + 2 * " + str(squares[i])
                    found = 1
                    break
        if found:
            break
        
        if not found:
            print(oddComposites[num])
            break

    endtime = time.clock()

    print("Took %f seconds" % (endtime - starttime))
        

prob(1000, 10000)

    

