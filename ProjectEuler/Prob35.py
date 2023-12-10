import math

primeBool = [True] * 1000000
primes = []

for i in range(2, 1001):
    for multiple in range(2, (1000000 / i)):
        primeBool[i * multiple] = False

"""
1000000 = i * multiple
"""

numCircularPrimes = 0

for i in range(2, 1000000):
    if primeBool[i] == True:
        primes.append(i)

for num in primes:
    newNum = num
    numPrimesInNum = 0
    
    for numRotations in range(int(math.ceil(math.log(num)))):
        
        if newNum in primes:
            numPrimesInNum = numPrimesInNum + 1
        
        remainder = num % 10
        newNum = num - remainder
        newNum = (newNum / 10) + ((numRotations - 1) * remainder)

    if numPrimesInNum == int(math.ceil(math.log(num))):
        numCircularPrimes = numCircularPrimes + 1
        
print(numCircularPrimes)
