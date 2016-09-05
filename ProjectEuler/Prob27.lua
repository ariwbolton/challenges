local math = require("math")

local sqrt = math.sqrt
local ceil = math.ceil
local abs = math.abs

-- Find all primes up to n
function primeSieve (n)
	primes = {}

	for i=2,n do
		primes[i] = true
	end

	for i=2,(ceil(sqrt(n)) + 1) do
		if primes[i] then
			for j=(2*i),n,i do
				primes[j] = false
			end
		end
	end

	return primes
end

function printPrimes(myTable)
	for k, v in pairs( myTable ) do
		if v then
			print(k)
		end
	end
end

-- n == 1000^2 + 1000^2 + 1000
local primes = primeSieve(2001000)

function run ()
	max = 0
	maxA, maxB = 0, 0

	for a=-999,999 do
		for b=-1000,1000 do
			numPrimes = test(a, b)

			if numPrimes > max then
				max = numPrimes
				maxA, maxB = a, b
			end
		end
	end

	print(maxA * maxB)
end

function test (a, b)
	numPrimes = 0

	for n=0,abs(b-1) do
		local f = ((n*n) + (a * n) + b)

		if primes[f] then
			numPrimes = numPrimes + 1
		else
			return numPrimes
		end
	end

	return numPrimes
end

run()