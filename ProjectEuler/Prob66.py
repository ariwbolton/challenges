import math
import cProfile

# iterate through increasing D
def calcVals():
    minX = list()
    maxD = int(0)
    
    for D in range(2, 100):
        if isSquare(D):
            minX.append(-1)
            continue

        currentMinX = int(math.sqrt(D)) + 1
        found = False

        x = int(currentMinX)

        # choose x^^2 - 1 to be multiples of D
        while not found:
            v = (x*x) - int(1)
            if x % 1000 == 0:
                #print x
                pass
                
            if v % D == 0 and isSquare(v / D):
                minX.append(x)
                if D > maxD:
                    maxD = D
                found = True
                print(D, x)
            else:
                x = x + 1

    return (maxD, minX)

def isSquare(x):
    s = int(math.sqrt(x))

    return x == (s * s)

cProfile.run('calcVals()')

#print minX
print(maxD)
        
    
        
