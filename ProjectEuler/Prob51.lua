local math = require("math")
local table = require("table")

local sqrt = math.sqrt
local ceil = math.ceil
local floor = math.floor
local abs = math.abs
local log = math.log

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

-- Convert n of digits-length to multiset of digits
function convertToSet (n, digits)
	local s = {}
	local temp = n
	local d

	for i=1,digits do
		d = n % 10

		if s[d] == nil then
			s[d] = 0
		end

		s[d] = s[d] + 1

		n = floor(n / 10)
	end

	return s
end

function printTable ( table, n )
	if next(table) == nil then
		return nil
	end

	print(n..":")

	for k, v in pairs( table ) do
		local s = "\t"..k..": ["

		for i, val in pairs(v) do
			s = s .. " " .. val .. ","
		end

		s = s .. "]"

		print(s)
	end
end

-- Generate sequences of indices of repeating digits
function repeating (val)
	local n = val
	local iTable = {}	-- Index table
	local index = 1

	-- Generate sequences 
	while n > 0 do
		d = n % 10

		if iTable[d] == nil then
			iTable[d] = {}
		end

		-- Append index
		table.insert(iTable[d], index)

		n = floor(n / 10)
		index = index + 1
	end

	-- Filter out single digits
	for i, v in pairs(iTable) do
		if #v <= 1 then
			iTable[i] = nil
		end
	end 

	return (#iTable == #{} and nil) or iTable
end

-- Compute all subsets
function subs (indexArray)
	
end

-- Test each n
function test (n)
	local r = repeating(n)

	if r[1] == nil and r[2] == nil then
		return false
	end

	for i, v in pairs(r) do
		local subs = subsets(n, v)
	end

	return false
end

--  Run
function run ()
	local continue = true
	local success = false

	for n=10,m do
		if primes[n] == true then
			success = test(n)
		end

		if success then
			print(n)
			break
		end
	end
end

-- Upper limir
m = 1000

primes = primeSieve(m)

run()

