import math

def isSquare(a, b):
    return a == b

def findNum(a, b):
    n, m, num = a, b, 0

    while (not isSquare(n, m)) and m != 0:
        #n, m = max(n - m, m), max(min(n - m, m), 0)
        
        #print "n = ", str(n), " : m = ", str(m)

        q = n / m

        m, n = (n - (q * m)), m
        num = num + q

    print num

inp = raw_input()
inp = inp.split()
inp = [int(n) for n in inp]


findNum(inp[0], inp[1])
