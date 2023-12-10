# Solved
import copy

# self written prime generating function
from sieve import sieve

# generate list of primes up to n
n = 10000
lenOfSet = 4
a = sieve(n*n)

print("Finished Sieve")

primes = [i for i in range(2, n*n) if a[i]]

print("Finished primes")

lowerPrimes = [i for i in primes if i <= n]


primeSet = set(primes)
primeDict = {x: set() for x in lowerPrimes}

def concatenablePrimes(a, b):
	# return True if a and b are concatenable
	s1, s2 = str(a), str(b)

	# compute two possible concatenations
	p1, p2 = int(s1+s2), int(s2+s1)

	return (p1 in primeSet) and (p2 in primeSet) 

for i in range(len(lowerPrimes) - 1):
	for j in range(i, len(lowerPrimes)):
		p1, p2 = lowerPrimes[i], lowerPrimes[j]

		if concatenablePrimes(p1, p2):
			primeDict[p1].add(p2)
			primeDict[p2].add(p1)

setsOfFive = list()

def constructLargerSet(currentSet, cSMutual):
	# currentSet is set of mutually concatenable primes, len(currentSet) <= 5
	# cSMutual is set of mutually concatenable primes to every prime
	# in currentSet

	# if len(currentSet) == 5, save currentSet
	if len(currentSet) == 5 and not currentSet in setsOfFive:
		setsOfFive.append(copy.deepcopy(currentSet))
		return True
	
	# if len < 5 and len(cSMutual) isn't sufficient to produce set of
	# 5, reject
	if len(cSMutual) + len(currentSet) < lenOfSet:
		#print currentSet, cSMutual
		return False

	# Try to add every member of cSMutual to currentSet
	cSMutualCopy = copy.deepcopy(cSMutual)

	while len(cSMutualCopy) > 0:
		mem = cSMutualCopy.pop()
	
		# temporarily add MCP
		currentSet.add(mem)

		# create new cSMutual set for new currentSet
		newSet = cSMutual & primeDict[mem]

		# constructLargerSet will reject if new cSMutual is too small 
		# call constructLargerSet
		constructLargerSet(currentSet, newSet)

		# remove MCP
		currentSet.discard(mem)

def runner():
	a = set()
	for x in lowerPrimes:
		print(x)
		a.add(x)
		constructLargerSet(a, primeDict[x])
		a.discard(x)

runner()

print(setsOfFive)
	

