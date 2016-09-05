local math = require("math")

local sqrt = math.sqrt
local ceil = math.ceil
local floor = math.floor
local abs = math.abs

function run ()
	local digits = 2
	local continue = true

	while continue do
		-- start at 10(0^(n-1))
		local st = 10^(digits - 1)
		local cur = st

		-- iterate over all possible digit-length numbers
		while 6 * cur < 10 * st and continue do
			continue = test(cur, digits)

			if continue ~= true then
				print(cur)
			else
				cur = cur + 1
			end
		end

		digits = digits + 1
	end
end

function test (n, digits)
	n1 = convertToSet(n, digits)
	n2 = convertToSet(2*n, digits)

	if notEqual(n1, n2) then
		return true
	end

	n3 = convertToSet(3*n, digits)

	if notEqual(n1, n3) then
		return true
	end

	n4 = convertToSet(4*n, digits)

	if notEqual(n1, n4) then
		return true
	end

	n5 = convertToSet(5*n, digits)

	if notEqual(n1, n5) then
		return true
	end

	n6 = convertToSet(6*n, digits)

	if notEqual(n1, n6) then
		return true
	end

	-- Success
	return false

end

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

function printSet (mySet)
	for k, v in pairs( mySet ) do
		print(k .. ":" .. v)
	end
end

function notEqual (s1, s2)
	if subset(s1, s2) and subset(s2, s1) then
		return false
	end

	return true
end

-- Checks if s1 is a subset of s2
function subset (s1, s2)
	for k, v in pairs( s1 ) do
		if s2[k] == nil or s1[k] > s2[k] then
			return false
		end
	end

	return true
end

run()