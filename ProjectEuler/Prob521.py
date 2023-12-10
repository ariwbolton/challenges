# Unsolved

import math

def modifiedSieve(n):
	# return array with a[i] == 0 if i is prime,
	# a[i] == smpf(i)

	array = [0] * (n + 1)

	for i in range(2, int(math.sqrt(n)) + 1):
		if i % 100 == 0:
			print("Sieve at:", i)

		if array[i] != 0:
			continue

		for j in range((i + i), n + 1, i):
			if array[j] == 0:
				array[j] = i

	return array

N = 10 ** 12
M = 10 ** 9
Sum = 0

array = modifiedSieve(10**8)

for i in range(2, len(array)):
	if i % 10000 == 0:
		print("Sum at:", i)
	if array[i] == 0:
		Sum = (Sum + i) % M
	else:
		Sum = (Sum + array[i]) % M


print(Sum)
