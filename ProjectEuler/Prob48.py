# num to mod by 
N = 10000000000

def runner():
    rem = 0
    
    for num in xrange(1, 1001):
        rem = (rem + findRem(num)) % N

    return rem

def findRem(num):
    r = 1

    for i in xrange(num):
        r = (r * num) % N

    return r

print runner()
