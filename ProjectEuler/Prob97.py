# num to mod by 
N = 10000000000

def runner():
	rem = findRem(2, 7830457)
	rem = (rem * 28433) % N
	rem = (rem + 1) % N
	
	return rem

def findRem(base, power):
	# find (base ** power) % N
    r = 1

    for i in xrange(power):
        r = (r * base) % N

    return r

print runner()
